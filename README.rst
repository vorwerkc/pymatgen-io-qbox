Pymatgen-analysis-myaddon
=========================

This is a (pymatgen)[https://pymatgen.org/] addon to parse input files for the
first-principles molecular dynamics code (qbox)[qboxcode.org]. The addon is
under active development and currently allows only for basic IO features. These
include:

* Generating qbox input files from pymatgen.Structure objects
* Reading qbox input file from file or string and extraction of the underlying
  structure into pymatgen.Structure

Installation
============

Once pymatgen is installed (see (here)[https://pymatgen.org/installation.html]),
the addon is installed by

```
git clone -b master git@github.com:vorwerkc/pymatgen-io-qbox.git
cd pymatgen-io-qbox/
pip install -e .
```

Usage
=====

A qboxinput object can be generated from a structure and a dictionary containing
the pseudopotentials as

```python
from pymatgen.core import Lattice, Structure
from pymatgen.io.qbox import QboxInput

# create CsCl structure from https://pymatgen.org/introduction.html#matgenie-examples
lattice = Lattice.cubic(4.2)
structure = Structure(lattice, ['Cs', 'Cl'],
                      [[0.0, 0.0, 0.0], [0.5, 0.5, 0.5]])

# define pseudopotential dict
pseudos = {'Cs': 'Cs_test.xml', 'Cl': 'Cl_test.xml'}

# create qbox input
qbox = QboxInput(structure, pseudos=pseudos)

# write qbox input file
qbox.write_file('example.i')
```

Alternatively, the object can be created from file and can be used to extract
the structure from the qbox input file

```
from pymatgen.io.qbox import QboxInput

# create qbox input from file
qbox = QboxInput.from_file('example.i')

# access the structure
print(qbox.structure)
```

