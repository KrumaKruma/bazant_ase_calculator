# Bazant ASE Calculator
This package contains the bazant silicon force field written in fortran and is interfaced to python to use it within the atomic simulation environment package.

## Installation
The package can either be installed directly via pip by execuding. Please consider that the python setup script need numpy to be preinstalled for proper installation.
```
pip install 'git+https://github.com/KrumaKruma/bazant_ase_calculator.git'
```
or it can be install from source:
```
git clone https://github.com/KrumaKruma/bazant_ase_calculator.git
cd bazant_ase_calculator
pip install .
```

## Testing and usage
A test program can be found in
```
test/test.py
```
and an input structure is in
```
data/Si_in.extxyz
```

