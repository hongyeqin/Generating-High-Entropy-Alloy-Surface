# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:07:30 2022

@author: hongye
"""

import cv2
img = cv2.imread('jinggekx.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('process1.tif', gray)