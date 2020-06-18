#!/usr/bin/env python
# coding: utf-8

# In[65]:


#import tensorflow as tf
# import torch
import tensorflow as tf
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
import cv2
import os


# In[56]:


def face_detect(image):
    img = plt.imread(image)

    detector = MTCNN()

    faces = detector.detect_faces(img)
    for face in faces:
        print(face)
    
face_detect('IMG_6670.JPG')


# In[61]:


def pixel_patch(face, image):
    im = Image.open(image)
    
    btw_eyes = (face['keypoints']['left_eye'][0] + (face['keypoints']['right_eye'][0] - face['keypoints']['left_eye'][0])/2, 
                face['keypoints']['left_eye'][1]) 
    
    forehead_patch = (btw_eyes[0], face['box'][1] + (btw_eyes[1] - face['box'][1])/2)
    
    # Setting the points for cropped image 
    left = forehead_patch[0]
    top = forehead_patch[1]
    right = forehead_patch[0] + 30
    bottom = forehead_patch[1]  + 30
  
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    
    patch = im.crop((left, top, right, bottom)) 
    patch.show()
    
    return patch
    
pixel_patch(face, 'IMG_6670.JPG')
#face['keypoints']['left_eye'][0] - face['keypoints']['right_eye'][0]


# In[66]:


from colorthief import ColorThief

def get_color(patch):
    
    avg_color_per_row = np.average(patch, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    print(avg_color)

patch = pixel_patch(face, 'IMG_6670.JPG')
get_color(patch)


# In[ ]:




