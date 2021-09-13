# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:08:37 2021

@author: win
"""
"""
This module only works for oxidation reaction.
"""

import os
import numpy as np 
import matplotlib.pyplot as plt


def get_lable(path):
    """
    
    """
    titles = []
    txts = [f for f in os.listdir(path) if f.endswith('.txt') and os.path.isfile(os.path.join(path, f))]
    for txt in txts:
        with open(txt, 'r') as f:
             lines = f.readlines() 
             title = lines[2].strip("File:").strip('\n').strip('.bin')
             titles.append(title)
             
    return  titles
def get_potential_range(path):
    lower_potential = []
    higher_potential = []
    txts = [f for f in os.listdir(path) if f.endswith('.txt') and os.path.isfile(os.path.join(path, f))]
    for txt in txts:
        with open(txt, 'r') as f:
             lines = f.readlines()
             high_potential = lines[9].strip('High E (V) = ')
             higher_potential.append(high_potential)
             low_potential =  lines[9].strip('Low E (V) = ')
             lower_potential.append(low_potential)
             max_potential = max(higher_potential)
             min_potential = min(lower_potential)
             
    return  max_potential, min_potential
    
def txt_remove_title(path): 
    """
    mechine : CHI760
    total data points: 0-400
    cv times : 4 times 0-0.1-0-0.1
    valid data:0.1-0 100-200 points
    file type:
        Aug. 23, 2021   11:26:53
        .....
        .....

        Potential/V, Current/A

        0.000, 1.149e-4
        .....
    return :
        0.000, 1.149e-4
        .....
        
    """
    path = path
    txts = [f for f in os.listdir(path) if f.endswith('.txt') and os.path.isfile(os.path.join(path, f))]
    for txt in txts:
        with open(txt, 'r') as f:
             lines = f.readlines()
             if lines[19].find('Ep') == -1:
                 with open(txt, 'w') as f:
                      f.write(''.join(lines[24:]))
             else:
                 with open(txt, 'w') as f:
                      f.write(''.join(lines[27:]))
                 
    return txts


def get_data(txt):
    """
    Get colum data seperately 
    primitive data type
    a, 1
    b, 2
    return x = [a, b]
           y = [1, 2]
    """
    x = []
    y = []
    f = open(txt)
    for line in f:
        line = line.strip('\n')
        line = line.split(',')
        x.append(float(line[0]))
        y.append(float(line[1]))     
    f.close()

    return x , y

def get_lsv_data(txt):
    
    x, y = get_data(txt)
    x_num = len(x)
    x_oxidation = []
    y_oxidation = []
    for i in range(int(x_num)//2):
        x_oxidation.append(x[i])
        y_oxidation.append(y[i])
    return x_oxidation, y_oxidation
    
def get_tafel_data(txt, surface_area, cv=None):
    if cv:
        x_oxidation, y_oxidation = get_lsv_data(txt)
    else:
        x_oxidation, y_oxidation = get_data(txt)
    
    x =  [np.abs(i) for i in x_oxidation]
    y =  [j*1000/surface_area for j in y_oxidation]
    x_tafel = []
    y_tafel = []
    index = []
    for j in y:
        if j >5 and j < 15:
            y_tafel.append(j)
            
    for data in y_tafel:
        index.append(y.index(data))
    
    
    for i in index:
        x_tafel.append(x[i])
    return  x_tafel, y_tafel
    


def plot_cv(txt,surface_area,label, SCE=None):
    x, y = get_data(txt)
    if SCE:
        x =  [i+1.067 for i in x]
        
    else:
        x = [i for i in x]
    y = [j*1000/surface_area for j in y]
    plt.xlabel('Potential (eV)')
    plt.ylabel('Current Density (mA/cm2)')
    plt.plot(x,y,label = label )
    plt.legend(loc='best', frameon=False)
    return x , y
        
def plot_tafel(txt, surface_area, label,cv=None, SCE=None):
    if cv: 
       x , y = get_tafel_data(txt, surface_area,cv=True)
    else:
        x , y = get_tafel_data(txt, surface_area)
    
    plt.xlabel('Potential (V vs SCE)')
    plt.ylabel('j (mA/cm2)')
    plt.plot(y,x,label = label )
    plt.legend(loc='best', frameon=False)
   

def liner_fitting(x, y):
    z1 = np.polyfit(x, y, 1)
    p1 = np.poly1d(z1)
    y_fit = p1(x)
    plot1 = plt.plot(x, y_fit)
    

if __name__ == '__main__':  
   surface_area = 0.25
   path = '.'
   label = get_lable(path)
   txt_remove_title(path)
   txts = [f for f in os.listdir(path) if f.endswith('.txt') and os.path.isfile(os.path.join(path, f))]
   txt_num = len(txts)
   for i in range(txt_num):
       plot_cv(txts[i], surface_area, label[i])
       plt.savefig('cv', dpi=800)
   plt.figure()  
   for i in range(txt_num):
       plot_tafel(txts[i], surface_area, label[i])
       plt.savefig('tafel', dpi=800)
   #a, b = get_tafel_data('7.5mmolNH4F-420-N-LSV-2 - 副本.txt', 0.25)   
   #x, y = plot_tafel(txts[0],0.25, '1', '2')
   #print(a)
   
   
   
       
           
       
       
   
