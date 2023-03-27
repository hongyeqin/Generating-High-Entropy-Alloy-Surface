# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 11:21:43 2022

@author: hongye chin
@email: 290720931@qq.com
"""


import cv2
from mayavi.mlab import *
import numpy as np



def pseudo_color_surface_plot(file):
    image = cv2.imread(file)
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    H,S,V= cv2.split(hsv)
    (h, w) = image.shape[:2]
    x = np.mgrid[0:h:1]
    y = np.mgrid[0:w:1]
    surf(x,y,V,colormap='RdBu')
    show()
    
def image_brightness_tunning(file, value):
    img = cv2.imread(file,0)
# 增加图像亮度
# 注意需要使用cv.add(),不能直接x+y
    res1 = np.uint8(np.clip((cv2.add(value*img,-30)), 0, 255))
# 增加图像对比度
    res2 = np.uint8(np.clip((cv2.add(value*img,0)), 0, 255))
    tmp = np.hstack((img, res1, res2))  # 三张图片横向合并（便于对比显示）

    cv2.imshow('image', tmp)
    cv2.waitKey(0)
    cv2.imwrite('SEM-process.png', res1)

# image_brightness_tunning('SEM.png', 1.5)
pseudo_color_surface_plot('TEM-post.png')
# def f(x, y):
#     sin, cos = np.sin, np.cos
#     return sin(x + y) + sin(2 * x - y) + cos(3 * x + 4 * y)

# x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
# # surf(x, y, f)
# # show()
# d = f(x,y)
# # print(d)
# # print(d.shape)
# # print(x.shape)
# # print(y.shape)
#     #cs = contour_surf(x, y, f, contour_z=0)
    

# image = cv2.imread('Ni.png')
# hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
# H,S,V= cv2.split(hsv)
# (h, w) = image.shape[:2]
# x, y  = np.mgrid[0:h:1,0:w:1]

# surf(x,y,V)
# show()

# print(cv2.__version__)
# import matplotlib.pyplot as plt
# img = cv2.imread('test_sem.tif')
# sr = cv2.dnn_superres.DnnSuperResImpl_create()

# path = "ESPCN_x4.pb"

# sr.readModel(path)

# sr.setModel("espcn", 4) # set the model by passing the value and the upsampling ratio

# result = sr.upsample(img) # upscale the input image

# resized = cv2.resize(img,dsize=None,fx=8,fy=8)

# plt.figure(figsize=(12,8))

# plt.subplot(1,3,1)

# 	# Original image

# plt.imshow(img[:,:,::-1])

# plt.subplot(1,3,2)

# 	# SR upscaled

# plt.imshow(result[:,:,::-1])

# plt.subplot(1,3,3)

# 	# OpenCV upscaled

# plt.imshow(resized[:,:,::-1])

# plt.show()
















