#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 07:48:24 2025

@author: donutman
"""

# Un essai de pilotage de webcam
# Tuto : https://www.youtube.com/watch?v=3N7fRURLz4A

# %reset -f # Only if run through Spyder (iPython)

import cv2
import numpy as np
from effects import effects
import pyvirtualcam as vc

# %% Common parameters

W, H = 800, 600 #  Frame dimensions

neffects = len(effects)
pos = 0

VIRTUAL_CAM = True


# %% Webcam initialization

cap = cv2.VideoCapture(0)

if VIRTUAL_CAM:
    out = vc.Camera(width=640, height=480, fps=20)

if cap.isOpened():
    print('Camera succesfully opened')
else:
    print("Cannot open camera")
    exit()


cap.set(cv2.CAP_PROP_FRAME_WIDTH, W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, H)



# %% Main loop

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    frame = cv2.flip(frame, 1)
    win = effects[pos](frame)
    
    # Display the resulting frame
    cv2.imshow('frame', win)
    
    if VIRTUAL_CAM:
        # Sending to the virtual cam...
        b, g, r = cv2.split(win)
        out.send( cv2.merge([r,g,b]))
        out.sleep_until_next_frame()
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
    if key == ord(' '):
        pos = (pos + 1) % neffects
        print('new pos : ', pos)
    
cap.release()
if VIRTUAL_CAM:
    out.close()
cv2.destroyAllWindows()
