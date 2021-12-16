# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:03:26 2021

@author: hongye
@email:290720931@qq.com
"""
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.db import connect

db = connect('bulk.db')
symb = ['Al', 'Ni', 'Cu', 'Pd', 'Ag', 'Pt', 'Au']
atoms = bulk('Al', 'fcc')
new = atoms.repeat(2) #supercell
atoms_ordinal = new.get_atomic_numbers() # get atoms ordinal
atoms_num = len(atoms_ordinal)

print(new, atoms_num)
def get_random_alloy(num_structure, host, **kwargs):
    
    file = {} # key : atoms name value : fraction 
    for key, value in kwargs.items():
        file[key] = value
        
    key_dict = []
    value_dict = []
    
    for key in file:
        key_dict.append(key)
        value_dict.append(file[key])
    dopant_species = len(key_dict)
    
    for i in range(num_structure):
        seed=1120210312+i*100
        #seed=3001223+1*100
        model = bulk(host, 'fcc')
        super_cell = model.repeat(3)
        atoms_ordinal = super_cell.get_atomic_numbers()
        atoms_num = len(atoms_ordinal)
        elements = super_cell.get_chemical_symbols()
        impurity = [] 
        np.random.seed(seed) # for repeat
        for j in range(dopant_species):
            impurity.append(np.round(atoms_num * value_dict[j]))
        for k in range(len(impurity)):    
            l=0
            while l < int(impurity[k]):
                r = np.random.rand()
                n = int(np.ceil(r*atoms_num-1))
                if elements[n] == host:
                    elements[n]=key_dict[k]
                    l=l+1
            super_cell.set_chemical_symbols(elements)
        db.write(super_cell)        
        super_cell.write('POSCAR{}'.format(i))
       
        
get_random_alloy(100, 'Al', Pt=0.1, Sn=0.2, Cu=0.1, Mg=0.2)


    
    
        
    
#atoms.calc = EMT()
#eos = calculate_eos(atoms)
#v, e, B = eos.fit()  # find minimum
# Do one more calculation at the minimu and write to database:
#atoms.cell *= (v / atoms.get_volume())**(1 / 3)
#atoms.get_potential_energy()
#db.write(atoms, bm=B)
a = [1,2,3]
for i in a:
    print(i)