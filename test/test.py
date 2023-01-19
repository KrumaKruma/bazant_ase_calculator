import numpy as np
from ase.io import read, write
from asebazant.bazant_calc import BazantCalculator

def main():
    atoms = read('../data/Si_in.extxyz')
    calc = BazantCalculator()
    atoms.calc = calc
    print("Stress:  \n", atoms.get_stress())
    print("Forces:  \n", atoms.get_forces())
    print("Energy:  \n", atoms.get_potential_energy())


    write("Si_out.ascii", atoms)


if __name__ == '__main__':
    main()


