# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:56:19 2021

@author: win
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
def get_dir_name(path):
    dir_name = os.listdir(path)
    return dir_name
            
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

        with open(txt, 'w') as f:
             f.write(''.join(lines[128:329]))
    return txts

#txt_remove_title('./') 
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

def get_scan_rate(path):
    txt_name = [f for f in os.listdir(path) if f.endswith('.txt')]
#print(txt.sort(key=lambda x: int(x[1][:])))
    name = [float(i.strip('.txt')) for i in txt_name]
    name.sort()
    return name
    
def get_current_density(txt,surface_area):
    x = [x for x in get_data(txt)[0]]
    y = [i*1000/surface_area for i in get_data(txt)[1]]
    return x, y

def return_Janodic_minus_Jcathodic(txt, surface_area):
    
    x, y = get_current_density(txt, surface_area)
    j10 = get_current_density(txt,surface_area)[1][50] - get_current_density(txt,surface_area)[1][150]
    if j10  < 0:
        return -j10
    if j10 > 0:
        return j10
    
def plot_cv(txt,surface_area,name):
    x , y = get_current_density(txt, surface_area)
    plt.xlabel('Potential (eV)')
    plt.ylabel('Current Density (mA/cm2)')
    plt.plot(x,y, label='{} mV/s'.format(name))
    #plt.legend(loc = 'best', fontsize=8, frameon=False)
    

    
    
if __name__ == '__main__':
    """
    Usage:
        file structure
        ecsa---
               |-----1---|10mv.txt ...100mv.txt
               |-----2
               |-----3
               |-----4
     if you want to add title on your graph please revise directory name  list
     for example:
         lable = ['Ni','NiSn','NiAl', 'NiFe']
    
    Remind: Ni CV data should be added at file 1 and so on
    
    """
   #txts = [f for f in os.listdir(path) if f.endswith('.txt') and os.path.isfile(os.path.join(path, f))
    surface_area = 0.25
    path = './'
    dir_name = os.listdir(path)
    dir_num = len(dir_name)
    for i in range(dir_num):
        os.chdir(dir_name[i])
        #txt_remove_title('.')  # For the first run of the program, you need to run this line
        
        #txts = [f for f in os.listdir('.') if f.endswith('.txt') and os.path.isfile(os.path.join('.', f))]
        txt_name = [f.strip('.txt') for f in os.listdir('.') if f.endswith('.txt')]
        txt_name_sort = [f for f in os.listdir('.') if f.endswith('.txt')]
        txt_name_sort.sort(key=lambda x: int(x.split('.')[0][:-1]))
        scan_rate = get_scan_rate('.')
        for j in range(len(txt_name_sort)):
            plot_cv(txt_name_sort[j],surface_area,txt_name_sort[j].split('.')[0])
            
        plt.legend(loc = 'best', fontsize=8, frameon=False)
            
        plt.savefig('cv', dpi=800)
        plt.figure()           
                       
        #txt_remove_title('.')
       
        os.chdir('../')
    #
    plt.figure()
    print(txt_name_sort)
    
    
    
    
    label = get_dir_name('.')
    for i in range(dir_num):
        os.chdir(dir_name[i])
        txts = [f for f in os.listdir('.') if f.endswith('.txt') and os.path.isfile(os.path.join('.', f))]
        txt_name = [f.strip('.txt') for f in os.listdir('.') if f.endswith('.txt')]
        
        x = [float(i) for i in np.sort(txt_name)]
        x = sorted(x)
        y = []       
        for j in range(len(txts)):
            y.append(return_Janodic_minus_Jcathodic(txts[j], surface_area))
            y = [data for data in np.sort(y)]
        plt.scatter(x, y, label = label[i])
        plt.legend(loc = 'upper left', frameon = False)
    #   plt.savefig(label[i], dpi=800)
    #        #y.append(return_Janodic_minus_Jcathodic(txts[i], 0.25))
    #        plot_ecsa_scatter(txts[i], 0.25, x, label[i])
        os.chdir('../')
        plt.savefig('ecsa', dpi=800)
    plt.figure()
    
 
        
        
        
    
            
            
            
        
        
        

           
    
    
    
    
    
    
    
    
    
    
    
