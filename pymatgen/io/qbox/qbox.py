# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

"""
Classes for reading/manipulating/writing qbox input files.
"""
import json
from pathlib import Path
import numpy as np
import scipy.constants as const
from monty.io import zopen
from monty.json import MSONable

from pymatgen.core import Structure, Element, Lattice

__author__ = "Christian Vorwerk"
__copyright__ = "Copyright 2021"
__version__ = "0.1"
__maintainer__ = "Christian Vorwerk"
__email__ = "vorwerk@uchicago.edu"
__status__ = "Development"
__date__ = "Dec 22, 2021"

bohr_in_A = const.value('Bohr radius') / 10**(-10)

# Loads element data from json file
# Same data as used in pymatgen.core.Element
with open(str(Path(__file__).absolute().parent / "periodic_table.json")) as f:
    _pt_data = json.load(f)

class QboxInput(MSONable):
    """
    Object to read, write, and parse Qbox input files.

    .. attribute:: structure

        Associated Structure.

    .. attribute :: pseudos

        Dict containing pseudopotential filename for each element.
    """

    def __init__(self, structure, pseudos=None):
        """
        Args:
            structure (Structure) :: Structure object.
            pseudos (dict) :: dict containing pseudopotential files for each
            element.
        """
        self.structure = structure
        if pseudos is not None:
            for species in self.structure.composition.keys():
                if str(species) not in pseudos:
                    raise QboxInputError("Missing %s in pseudo specification!" % species)
            self.pseudos = pseudos

    @staticmethod
    def _element_from_long_name(longname: str):
        """
        Returns an element from the long name, i.e. "Silicon".

        Args:
            longname (str) : Long name of element, starting with either a lower-
            or upper-case letter.

        Returns:
            Element
        """
        if longname[0].islower():
            longname = longname[0].upper() + longname[1:]
        output = None
        for key in _pt_data.keys():
            if _pt_data[key]["Name"] == longname:
                output = Element(key)
                break
        return output

    @staticmethod
    def _is_valid_long_name(longname: str) -> bool:
        """
        Returns true if symbol is a valid long name.
        Args:
            symbol (str): Element long name
        Returns:
            True if symbol is a valid long name (e.g., "Silicon"). False
            otherwise (e.g., "Zebra").
        """
        if longname[0].islower():
            longname = longname[0].upper() + longname[1:]

        val = False
        for key in _pt_data.keys():
            if _pt_data[key]["Name"] == longname:
                val = True
                break
        return val

    @classmethod
    def from_file(cls, file):
        """
        Read QboxInput object from file.

        Args:
            file (str) :: filename.
        """
        # species and coordinates of each atomic site
        species_ = []
        coords_ = []
        # pseudopotential for each species
        pseudos = {}
        # species_map stores the mapping between the species name used in the
        # qbox input file and the Element.symbol as defined within pymatgen
        species_map = {}
        # intermediate pseudo_ list used to construct the site_properties for
        # the Structure object
        pseudos_ = []
        with open(file, 'r') as f:
            # first loop over lines to find lattice and all pseudopotentials
            for line in f.readlines():
                if 'set' in line.split() and 'cell' in line.split():
                    a = [float(entry)*bohr_in_A for entry in line.split()[2:5]]
                    b = [float(entry)*bohr_in_A for entry in line.split()[5:8]]
                    c = [float(entry)*bohr_in_A for entry in line.split()[8:11]]
                    lattice_ = Lattice([a, b, c])

                if line.split()[0] == 'species':
                    if Element.is_valid_symbol(line.split()[1]):
                        element_ = Element(line.split()[1])
                    elif QboxInput._is_valid_long_name(line.split()[1]):
                        element_ = QboxInput._element_from_long_name(line.split()[1])

                    pseudos[element_.symbol] = line.split()[-1]
                    species_map[line.split()[1]] = element_.symbol

            # second loop over lines to obtain atomic positions and assign
            # pseudos
            # go back to beginning of file
            f.seek(0)
            for line in f.readlines():
                if 'atom' in line.split():
                    if Element.is_valid_symbol(line.split()[2]):
                        species_.append(Element(line.split()[2]))
                    elif QboxInput._is_valid_long_name(line.split()[2]):
                        species_.append(QboxInput._element_from_long_name(line.split()[2]))

                    coords_.append([float(entry)*bohr_in_A for entry in line.split()[3:6]])
                    pseudos_.append(pseudos[species_map[line.split()[2]]])

        site_props = {'pseudo': pseudos_}
        structure = Structure(lattice_, species_, coords_, site_properties=
                site_props, coords_are_cartesian= True)
        return cls(structure, pseudos)

    def __str__(self):

        # set structure
        string = 'set cell '
        for vector in self.structure.lattice._matrix.tolist():
            for entry in vector:
                string += str(entry/bohr_in_A)+' '
        string += '\n'

        # add pseudopotential
        if self.pseudos is not None:
            for key in self.pseudos.keys():
                string += 'species '+str(key)+' '+ self.pseudos[key] + '\n'

        # add atoms
        i = 0
        for site in self.structure.sites:
            i += 1
            string += 'atom '+site.species.elements[0].symbol+str(i) + ' ' + site.species_string + ' '
            for entry in site.coords:
                string += str(entry/bohr_in_A) + ' '
            string += '\n'

        return string

    def write_file(self, filename):
        """
        Write the Qbox input file.

        Args:
            filename (str): The string filename to output to.
        """
        with open(filename, "w") as f:
            f.write(self.__str__())


class QboxInputError(BaseException):
    """
    Error for QboxInput
    """

    pass
