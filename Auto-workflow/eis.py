# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 15:39:53 2021

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
             
    return  titles
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
             f.write(''.join(lines[20:]))
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
    Freq = []
    Z_dot = []
    Z_double_dot = []
    Z_real = []
    Z_Im = []
    f = open(txt)
    for line in f:
        line = line.strip('\n')
        line = line.split(',')
        Freq.append(float(line[0]))
        Z_dot.append(float(line[1]))
        Z_double_dot.append(float(line[2]))
        Z_real.append(float(line[3]))
        Z_Im.append(float(line[4]))    
    f.close()
    return Freq , Z_dot, Z_double_dot, Z_real, Z_Im

def get_eis_data(txt):
    Z_dot, Z_double_dot = get_data(txt)[1], get_data(txt)[2]
    Z_double_dot_value = []
    Z_double_dot_index = []
    Z_dot_value = []
    
    for i in Z_double_dot:
        if float(i) < 0:
           Z_double_dot_value.append(i)
    for data in Z_double_dot_value:
        Z_double_dot_index.append(Z_double_dot.index(data))
    
    
    for i in Z_double_dot_index:
        Z_dot_value.append(Z_dot[i])
    return Z_dot_value, Z_double_dot_value

def get_bode_data(txt):
    
    Z_real, Z_Im = get_data(txt)[0], get_data(txt)[4]
    Z_Im_index = []
    Z_real_value = []
    Z_Im_value = []
    for i in Z_Im:
        if float(i) < 0:
            Z_Im_value.append(i)
    for data in Z_Im_value:
        Z_Im_index.append(Z_Im.index(data))
    
    for i in Z_Im_index:
        Z_real_value.append(Z_real[i])
        
    
    return Z_real_value, Z_Im_value
    
def plot_eis(txt, label):
    x, y = get_eis_data(txt)
    y = [np.abs(i) for i in y]
    plt.plot(x, y, label=label)
    plt.legend(loc='best', frameon=False)

def plot_bode(txt, label):
    x, y = get_bode_data(txt)
    x = [np.log10(i) for i in x]
    y = [np.abs(i) for i in y]
    plt.plot(x, y, label=label)
    plt.legend(loc='best', frameon=False)
    return x , y
    

if __name__ == '__main__':
    

   path = '.'
   label = get_lable(path)
   txt_remove_title(path)
   txts = [f for f in os.listdir(path) if f.endswith('.txt') and os.path.isfile(os.path.join(path, f))]
   txt_num = len(txts) 
   for i in range(txt_num):
       plot_eis(txts[i], label[i])
       plt.savefig('eis', dpi=800)
   plt.figure()
   
   for i in range(txt_num):
       plot_bode(txts[i], label[i])
       plt.savefig('bode', dpi=800)
   
   


   
       
   


           
