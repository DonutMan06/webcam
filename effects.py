#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 13:29:22 2025

@author: donutman
"""

import numpy as np
import cv2

ascii_chars = ' `.-\':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@'
ascii = list(ascii_chars)

n = len(ascii)

font = cv2.FONT_HERSHEY_SIMPLEX

cW, cH = 12, 12 # Cell dimensions...

ratio = 6 # ratio factor for horizontalCycle... (bigger means faster but more pixelated)

R_cycle = np.zeros((int(480/ratio),int(640/ratio),int(480/ratio)+1), np.uint8) # hard-coded values of W and H, i'm ashamed...
G_cycle = np.zeros((int(480/ratio),int(640/ratio),int(480/ratio)+1), np.uint8)
B_cycle = np.zeros((int(480/ratio),int(640/ratio),int(480/ratio)+1), np.uint8)

def effect_simplecircle(image):
    H, W, _ = image.shape;
    W2, H2 = int(W/cW), int(H/cH)
    
    #black_window = np.zeros( (H, W, 3), np.uint8)
    black_window = np.ones( (H, W, 3), np.uint8)*48
    
    small_image = cv2.resize(image, (W2, H2), interpolation=cv2.INTER_NEAREST)
    
    for i in range(H2):
        for j in range(W2):
            color = small_image[i, j]
            b = int(color[0])
            g = int(color[1])
            r = int(color[2])
            
            # print(r, g, b) # Chacun entre 0 et 255
            
            # Formula from https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
            intensity = (0.2126*r + 0.7152*g + 0.0722*b)
            
            # Interisting, we have : 0 <= intensity <= 255
            
            index = int(intensity/255*n)
            
            char = ascii[index]
            
            cX = j*cW+cW # Center coordinates of circle
            cY = i*cH
            
            # image, (centerX, centerY), radius, color, thickness
            
            cv2.circle(black_window, (cX, cY), 5, (b,g,r), 2)
            
    return black_window



def effect_varcircle(image):
    H, W, _ = image.shape;
    W2, H2 = int(W/cW), int(H/cH)
    
    #black_window = np.zeros( (H, W, 3), np.uint8)
    black_window = np.ones( (H, W, 3), np.uint8)*48
    
    small_image = cv2.resize(image, (W2, H2), interpolation=cv2.INTER_NEAREST)
    
    for i in range(H2):
        for j in range(W2):
            color = small_image[i, j]
            b = int(color[0])
            g = int(color[1])
            r = int(color[2])
            
            # print(r, g, b) # Chacun entre 0 et 255
            
            # Formula from https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
            intensity = (0.2126*r + 0.7152*g + 0.0722*b)
            
            # Interisting, we have : 0 <= intensity <= 255
            
            index = int(intensity/255*n)
            
            char = ascii[index]
            
            cX = j*cW+cW # Center coordinates of circle
            cY = i*cH
            
            # image, (centerX, centerY), radius, color, thickness
            
            #cv2.circle(black_window, (cX, cY), 5, (b,g,r), 2)
            #cv2.circle(black_window, (cX, cY), 5, (0, int(0.25*g), 0), 2)
    
            #cv2.putText(black_window, char, (cX, cY), font, 0.4, (0,150,0), 1, cv2.LINE_AA)
            
            cv2.circle(black_window, (cX, cY), int(intensity*0.5*cW/255), (0, 175, 0), -1)
            
    return black_window





        
def effect_hckr(image):
    H, W, _ = image.shape;
    W2, H2 = int(W/cW), int(H/cH)
    
    #black_window = np.zeros( (H, W, 3), np.uint8)
    black_window = np.ones( (H, W, 3), np.uint8)*48
    
    small_image = cv2.resize(image, (W2, H2), interpolation=cv2.INTER_NEAREST)
    
    for i in range(H2):
        for j in range(W2):
            color = small_image[i, j]
            b = int(color[0])
            g = int(color[1])
            r = int(color[2])
            
            # print(r, g, b) # Chacun entre 0 et 255
            
            # Formula from https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
            intensity = (0.2126*r + 0.7152*g + 0.0722*b)
            
            # Interisting, we have : 0 <= intensity <= 255
            
            index = int(intensity/255*n)
            
            char = ascii[index]
            
            cX = j*cW+cW # Center coordinates of circle
            cY = i*cH
             
            cv2.putText(black_window, char, (cX, cY), font, 0.4, (0,150,0), 1, cv2.LINE_AA)

            
    return black_window



def horizontalCycle(image):
    
    global R_cycle, G_cycle, B_cycle
    H, W, _ = image.shape;
    W2, H2 = int(W/ratio), int(H/ratio)
    
    small_image = cv2.resize(image, (W2, H2), interpolation=cv2.INTER_NEAREST)
    
    b, g, r = cv2.split(small_image)
    
    print('r shape = ', r.shape)
    print('R_cycle : ', R_cycle.shape)

    for i in range(R_cycle.shape[0]):
        #print('DEBUG : R_cycle = %s et r = %s' % (R_cycle[i,:,i].shape, r[i,:].shape))
        R_cycle[i,:,i] = r[i,:]
        G_cycle[i,:,i] = g[i,:]
        B_cycle[i,:,i] = b[i,:]
    
    # Now we extract the very first slice
    currentR = R_cycle[:,:,0]
    currentG = G_cycle[:,:,0]
    currentB = B_cycle[:,:,0]
    
    # We delete the first slice as well, and we add a black screen at the end
    R_cycle = np.delete(R_cycle, 0, axis = 2)
    G_cycle = np.delete(G_cycle, 0, axis = 2)
    B_cycle = np.delete(B_cycle, 0, axis = 2)
    print('A : ', R_cycle.shape)
    
    
    s = (R_cycle.shape[0], R_cycle.shape[1], 1)
    print('Trying to add a slice a the end with shape = ', s)
    R_cycle = np.append(R_cycle, np.zeros(s, 'uint8'), axis=2)
    G_cycle = np.append(G_cycle, np.zeros(s, 'uint8'), axis=2)
    B_cycle = np.append(B_cycle, np.zeros(s, 'uint8'), axis=2)
    print('B : ', R_cycle.shape)
    
    small_image = cv2.merge([currentB, currentG, currentR])
    
    return cv2.resize(small_image, (W, H), interpolation=cv2.INTER_NEAREST)
    
    
    


effects = [effect_simplecircle, effect_varcircle, effect_hckr, horizontalCycle]

