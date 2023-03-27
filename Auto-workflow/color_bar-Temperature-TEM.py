# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:24:15 2022

@author: hongye qin
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt 
name = 'e_xy1.tif'
image = cv2.imread(name,cv2.IMREAD_COLOR)

image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


(h, w) = image1.shape[:2]
x = np.mgrid[0:h:1]
y = np.mgrid[0:w:1]
rgb_list = []
for i in x:
    for j in y:
        rgb = image1[i,j]
        rgb_list.append(rgb)
        

blue = [[0.0, 3.0, 250.0], [0.0, 7.0, 245.0], [0.0, 10.0, 240.0], [0.0, 13.0, 235.0], [0.0, 17.0, 230.0], [0.0, 20.0, 225.0], [0.0, 23.0, 220.0], [0.0, 27.0, 215.0], [0.0, 30.0, 210.0], [0.0, 33.0, 205.0], [0.0, 37.0, 200.0], [0.0, 40.0, 195.0], [0.0, 43.0, 190.0], [0.0, 47.0, 185.0], [0.0, 50.0, 180.0], [0.0, 53.0, 175.0], [0.0, 57.0, 170.0], [0.0, 60.0, 165.0], [0.0, 63.0, 160.0], [0.0, 67.0, 155.0], [0.0, 70.0, 150.0], [0.0, 73.0, 145.0], [0.0, 77.0, 140.0], [0.0, 80.0, 135.0], [0.0, 83.0, 130.0], [0.0, 87.0, 125.0], [0.0, 90.0, 120.0], [0.0, 93.0, 115.0], [0.0, 97.0, 110.0], [0.0, 100.0, 105.0], [0.0, 103.0, 100.0], [0.0, 107.0, 95.0], [0.0, 110.0, 90.0], [0.0, 113.0, 85.0], [0.0, 117.0, 80.0], [0.0, 120.0, 75.0], [0.0, 123.0, 70.0], [0.0, 127.0, 65.0], [0.0, 130.0, 60.0], [0.0, 133.0, 55.0], [0.0, 137.0, 50.0], [0.0, 140.0, 45.0], [0.0, 143.0, 40.0], [0.0, 147.0, 35.0], [0.0, 150.0, 30.0], [0.0, 153.0, 25.0], [0.0, 157.0, 20.0], [0.0, 160.0, 15.0], [0.0, 163.0, 10.0], [0.0, 167.0, 5.0], [0.0, 170.0, 0.0]]
green = [[5.0, 167.0, 0.0], [10.0, 163.0, 0.0], [15.0, 160.0, 0.0], [20.0, 157.0, 0.0], [25.0, 153.0, 0.0], [30.0, 150.0, 0.0], [35.0, 147.0, 0.0], [40.0, 143.0, 0.0], [45.0, 140.0, 0.0], [50.0, 137.0, 0.0], [55.0, 133.0, 0.0], [60.0, 130.0, 0.0], [65.0, 127.0, 0.0], [70.0, 123.0, 0.0], [75.0, 120.0, 0.0], [80.0, 117.0, 0.0], [85.0, 113.0, 0.0], [90.0, 110.0, 0.0], [95.0, 107.0, 0.0], [100.0, 103.0, 0.0], [105.0, 100.0, 0.0], [110.0, 97.0, 0.0], [115.0, 93.0, 0.0], [120.0, 90.0, 0.0], [125.0, 87.0, 0.0], [130.0, 83.0, 0.0], [135.0, 80.0, 0.0], [140.0, 77.0, 0.0], [145.0, 73.0, 0.0], [150.0, 70.0, 0.0], [155.0, 67.0, 0.0], [160.0, 63.0, 0.0], [165.0, 60.0, 0.0], [170.0, 57.0, 0.0], [175.0, 53.0, 0.0], [180.0, 50.0, 0.0], [185.0, 47.0, 0.0], [190.0, 43.0, 0.0], [195.0, 40.0, 0.0], [200.0, 37.0, 0.0], [205.0, 33.0, 0.0], [210.0, 30.0, 0.0], [215.0, 27.0, 0.0], [220.0, 23.0, 0.0], [225.0, 20.0, 0.0], [230.0, 17.0, 0.0], [235.0, 13.0, 0.0], [240.0, 10.0, 0.0], [245.0, 7.0, 0.0], [250.0, 3.0, 0.0], [255.0, 0.0, 0.0]]
black = [[0.0, 0.0, 0.0], [0.0, 0.0, 5.0], [0.0, 0.0, 10.0], [0.0, 0.0, 15.0], [0.0, 0.0, 20.0], [0.0, 0.0, 25.0], [0.0, 0.0, 30.0], [0.0, 0.0, 35.0], [0.0, 0.0, 40.0], [0.0, 0.0, 45.0], [0.0, 0.0, 50.0], [0.0, 0.0, 55.0], [0.0, 0.0, 60.0], [0.0, 0.0, 65.0], [0.0, 0.0, 70.0], [0.0, 0.0, 75.0], [0.0, 0.0, 80.0], [0.0, 0.0, 85.0], [0.0, 0.0, 90.0], [0.0, 0.0, 95.0], [0.0, 0.0, 100.0], [0.0, 0.0, 105.0], [0.0, 0.0, 110.0], [0.0, 0.0, 115.0], [0.0, 0.0, 120.0], [0.0, 0.0, 125.0], [0.0, 0.0, 130.0], [0.0, 0.0, 135.0], [0.0, 0.0, 140.0], [0.0, 0.0, 145.0], [0.0, 0.0, 150.0], [0.0, 0.0, 155.0], [0.0, 0.0, 160.0], [0.0, 0.0, 165.0], [0.0, 0.0, 170.0], [0.0, 0.0, 175.0], [0.0, 0.0, 180.0], [0.0, 0.0, 185.0], [0.0, 0.0, 190.0], [0.0, 0.0, 195.0], [0.0, 0.0, 200.0], [0.0, 0.0, 205.0], [0.0, 0.0, 210.0], [0.0, 0.0, 215.0], [0.0, 0.0, 220.0], [0.0, 0.0, 225.0], [0.0, 0.0, 230.0], [0.0, 0.0, 235.0], [0.0, 0.0, 240.0], [0.0, 0.0, 245.0], [0.0, 0.0, 250.0], [0.0, 0.0, 255.0]]
yellow = [[255.0, 5.0, 0.0], [255.0, 10.0, 0.0], [255.0, 15.0, 0.0], [255.0, 20.0, 0.0], [255.0, 25.0, 0.0], [255.0, 30.0, 0.0], [255.0, 35.0, 0.0], [255.0, 40.0, 0.0], [255.0, 45.0, 0.0], [255.0, 50.0, 0.0], [255.0, 55.0, 0.0], [255.0, 60.0, 0.0], [255.0, 65.0, 0.0], [255.0, 70.0, 0.0], [255.0, 75.0, 0.0], [255.0, 80.0, 0.0], [255.0, 85.0, 0.0], [255.0, 90.0, 0.0], [255.0, 95.0, 0.0], [255.0, 100.0, 0.0], [255.0, 105.0, 0.0], [255.0, 110.0, 0.0], [255.0, 115.0, 0.0], [255.0, 120.0, 0.0], [255.0, 125.0, 0.0], [255.0, 130.0, 0.0], [255.0, 135.0, 0.0], [255.0, 140.0, 0.0], [255.0, 145.0, 0.0], [255.0, 150.0, 0.0], [255.0, 155.0, 0.0], [255.0, 160.0, 0.0], [255.0, 165.0, 0.0], [255.0, 170.0, 0.0], [255.0, 175.0, 0.0], [255.0, 180.0, 0.0], [255.0, 185.0, 0.0], [255.0, 190.0, 0.0], [255.0, 195.0, 0.0], [255.0, 200.0, 0.0], [255.0, 205.0, 0.0], [255.0, 210.0, 0.0], [255.0, 215.0, 0.0], [255.0, 220.0, 0.0], [255.0, 225.0, 0.0], [255.0, 230.0, 0.0], [255.0, 235.0, 0.0], [255.0, 240.0, 0.0], [255.0, 245.0, 0.0], [255.0, 250.0, 0.0], [255.0, 255.0, 0.0]]
white = [[255.0, 255.0, 5.0], [255.0, 255.0, 10.0], [255.0, 255.0, 15.0], [255.0, 255.0, 20.0], [255.0, 255.0, 25.0], [255.0, 255.0, 30.0], [255.0, 255.0, 35.0], [255.0, 255.0, 40.0], [255.0, 255.0, 45.0], [255.0, 255.0, 50.0], [255.0, 255.0, 55.0], [255.0, 255.0, 60.0], [255.0, 255.0, 65.0], [255.0, 255.0, 70.0], [255.0, 255.0, 75.0], [255.0, 255.0, 80.0], [255.0, 255.0, 85.0], [255.0, 255.0, 90.0], [255.0, 255.0, 95.0], [255.0, 255.0, 100.0], [255.0, 255.0, 105.0], [255.0, 255.0, 110.0], [255.0, 255.0, 115.0], [255.0, 255.0, 120.0], [255.0, 255.0, 125.0], [255.0, 255.0, 130.0], [255.0, 255.0, 135.0], [255.0, 255.0, 140.0], [255.0, 255.0, 145.0], [255.0, 255.0, 150.0], [255.0, 255.0, 155.0], [255.0, 255.0, 160.0], [255.0, 255.0, 165.0], [255.0, 255.0, 170.0], [255.0, 255.0, 175.0], [255.0, 255.0, 180.0], [255.0, 255.0, 185.0], [255.0, 255.0, 190.0], [255.0, 255.0, 195.0], [255.0, 255.0, 200.0], [255.0, 255.0, 205.0], [255.0, 255.0, 210.0], [255.0, 255.0, 215.0], [255.0, 255.0, 220.0], [255.0, 255.0, 225.0], [255.0, 255.0, 230.0], [255.0, 255.0, 235.0], [255.0, 255.0, 240.0], [255.0, 255.0, 245.0], [255.0, 255.0, 250.0], [255.0, 255.0, 255.0]]

color_bar = black + blue + green + yellow + white
# print(len(color_bar)) 
# array = np.array(color_bar).reshape((16,16,3))
# print(array)  
   
# x = np.mgrid[0:16:1]
# y = np.mgrid[0:16:1]  
def elur_distance(m,n):
    
    return np.sqrt(np.sum((m - n) ** 2))
x = np.linspace(-1,1, num=256).tolist()  
assert len(x) == len(color_bar)
color_dict = dict(zip(x, color_bar))

def confirm_piex(a,color_dict):
    
    for i in color_dict:
        
        if abs(i[0] - a[0]) <2 and abs(int(i[1]) - int(a[1])) < 2 and abs(int(i[2]) - int(a[2])) < 2:
        # if abs((int(i[0]) - int(a[0])) < 2:
            
           return i

def moment(x, y, n):
    """moments function to calculate the porbability distribution characteristics of density of states.
    Args:
       x (array): energy values
       y (array): density of states
       n (int): order parameter of moments function
    Returns:
       float: moment descriptor 
    """
    p = x**n * y
    return np.trapz(p, x)/np.trapz(y, x)
def center(x,y):
    p = np.multiply(x,y)
#    s = np.multiply(p,x)
    return sum(p)/sum(y)

def count_intensity(min_strain, max_strain, color_bar, image_list):
    
    """
    Usage: max_strain 0.1 tensile
           min_strain -0.1 stress
        
    """
    
    counts = []
    x = np.linspace(min_strain,max_strain, num=256).tolist()
    color_dict = dict(zip(x, color_bar))
    for i in image_list:
        new_color = confirm_piex(i, color_bar)
        
        for key, value in color_dict.items():
            if new_color == value:
                counts.append(key)
    intensity = {}
    strain = [] 
    count = []

    # avarage = moment(np.array(strain), np.array(count), 1)
    counts = tuple(counts)
    for i in counts:
        intensity[i] = counts.count(i)
    for k, v in intensity.items():
        strain.append(k)
        count.append(v)    
    barycenter = center(np.array(strain)*100, np.array(count))
    plt.figure(figsize=(7,6))
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_linewidth(5)
    ax.spines['top'].set_linewidth(5)
    ax.spines['right'].set_linewidth(5)
    plt.bar(np.array(strain)*100, np.array(count),width=(max_strain*100-min_strain*100)/len(color_bar))
    plt.ylabel('Intensity (a.u.)',size=20)
    plt.yticks([])
    plt.xlabel('Strain (%)',size=20)
    plt.axvline(x=barycenter, c='r', ls='--', lw=2, label='$\epsilon$ = %.2f'%barycenter)
    plt.legend()
    plt.savefig('strain-{}'.format(name), dpi=1000)
    plt.show()

        
                
    
f = count_intensity(-0.2, 0.2, color_bar, rgb_list)
    
    
   



    









