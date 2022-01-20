# coding: utf-8
# Copyright (c) Materials Virtual Lab
# Distributed under the terms of the Modified BSD License.

from setuptools import setup, find_namespace_packages

import os

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SETUP_PTH, "README.md")) as f:
    desc = f.read()


setup(
    name="pymatgen-io-qbox",
    packages=find_namespace_packages(include=["pymatgen.io.*"]),
    version="0.0.1",
    install_requires=["pymatgen>=2022.0.3"],
    extras_require={},
    package_data={},
    author="Christian Vorwerk",
    author_email="vorwerk@uchicago.edu",
    maintainer="Christian Vorwerk",
    url="https://github.com/materialsproject/pymatgen-addon-template",
    license="MIT",
    description="Functions to import and export QBOX input files with pymatgen.",
    long_description=desc,
    keywords=["pymatgen"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
