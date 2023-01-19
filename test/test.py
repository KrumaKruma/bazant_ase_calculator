import numpy as np
from ase.io import read, write
from bazant_calc import BazantCalculator

def lattice_derivative(atoms):
    #BAZANT TEST
    #______________________________________________________________________________________
    #e_pot, forces, deralat, stress_tensor = energyandforces(atoms)
    stress_tensor = atoms.get_stress(voigt=False,apply_constraint=False)
    #______________________________________________________________________________________
    cell = atoms.get_cell(complete=False)

    inv_cell = np.linalg.inv(cell)
    prefact = np.linalg.det(cell)
    deralat = - prefact * np.matmul(stress_tensor, inv_cell).T
    return deralat

def main():
    atoms = read('../../data/Si_in.extxyz')
    calc = BazantCalculator()
    atoms.calc = calc
    print("Stress:  \n", atoms.get_stress())
    print("Forces:  \n", atoms.get_forces())
    print("Energy:  \n", atoms.get_potential_energy())

    deralat = lattice_derivative(atoms)
    print("Lattice derivative:   \n", deralat)


    write("Si_out.ascii", atoms)


if __name__ == '__main__':
    main()


