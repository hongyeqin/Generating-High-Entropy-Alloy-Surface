# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:38:08 2021

@author: Hongye Qin
@email : 290720931@qq.com
"""
from matplotlib import pyplot as plt
import numpy as np
import argparse

# Raster equal to 1200 , static mode. renishaw raman

parser = argparse.ArgumentParser(description='Input basic variable,such as surface area, cv range')
parser.add_argument('--index','-i', type=float, default=521, help='please input wave number index')
parser.add_argument('--path', '-p', type=str, default='.', help='Please input working directory')
args = parser.parse_args()
index = args.index
path = args.path

def get_data(file):
    """
    get x , y coordinate, total points, wave numbers, intensity
    
    """
    x = []
    y = []
    wave = []
    intensity = []
    wave = []
    intensity = []
    index_xi = []
    f = open(file)
    for line in f:
        line = line.strip('\n')
        line = line.split('\t')
        x.append(float(line[0]))
        y.append(float(line[1])) 
        wave.append(float(line[2]))
        intensity.append(float(line[3]))
        
    f.close()
    y_list = list(set(y))
    y_list.sort(key = y.index)
    x_list = list(set(x))
    x_list.sort(key = x.index)
    
    p = len(wave)
    for i in range(p-1):
        if wave[i+1] > wave[i]:
           index_xi.append(i+1)
           
    wave_list = list(set(wave))
    wave_list.sort(key = wave.index)
    total_points = len(x)/index_xi[0] # The number of collected data points
    return   x_list, y_list, total_points, wave_list, intensity
def get_wave_relevent_intensity(file,index):
    """
    index: which means the data needs to manipulate
    for examples:
        1 10
        2 30
        3 40
    1, 2,3 stands for wave numbers, 10 20 30 stands for intensity
    the index of 1 is 0 and so on and forth
    
    """
    total_points = get_data(file)[2]
    intensity = get_data(file)[4]
    intensity_with_relevent_wave = []
    for i in range(int(total_points)):
        intensity_with_relevent_wave.append(intensity[index+i*1015])
        
        
    
    return intensity_with_relevent_wave

def plot_hotmap(x, y , valuable):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_yticks(y)
    ax.set_xticks(x)
    im = ax.imshow(valuable, cmap = plt.cm.hot_r)
    plt.colorbar(im)
    plt.show()   
          

   
x = get_data('1.txt')[0]
y = get_data('1.txt')[1]
valuable = get_wave_relevent_intensity('1.txt', 328) 
# it is necessary to change 768 to any index that you want research
valuable = np.array(valuable, dtype=np.float64).reshape(len(y),len(x))
plt.imshow(valuable, interpolation="gaussian", extent=[0, max(x)-min(x), max(y)-min(y), 0])
plt.colorbar()
#plt.savefig('mapping.png', dpi = 600)

import seaborn as sns
ax = sns.heatmap(valuable, vmin=7000, vmax=17000)

    
    
    