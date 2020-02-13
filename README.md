import os
import warnings
warnings.simplefilter('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.color import rgb2gray
rajini=os.listdir(r"C:\Users\students\Desktop\Images_srm\Images_srm\rajinikanth")
vijay=os.listdir(r"C:\Users\students\Desktop\Images_srm\Images_srm\vijay")
dhanush=os.listdir(r"C:\Users\students\Desktop\Images_srm\Images_srm\dhanush")
limit=100
rajini_images=[None]*limit
j=0
for i in rajini:
    if(j<limit):
        rajini_images[j]=imread(r"C:\Users\students\Desktop\Images_srm\Images_srm\rajinikanth/"+i)
        j+=1
    else:
        break
        vijay_images=[None]*limit
j=0
for i in vijay:
    if(j<limit):
        vijay_images[j]=imread(r"C:\Users\students\Desktop\Images_srm\Images_srm\vijay/"+i)
        j+=1
    else:
        break
        dhanush_images=[None]*limit
j=0
for i in dhanush:
    if(j<limit):
        dhanush_images[j]=imread(r"C:\Users\students\Desktop\Images_srm\Images_srm\dhanush/"+i)
        j+=1
    else:
        break
        imshow(rajini_images[1])
        imshow(dhanush_images[1])
        imshow(vijay_images[10])
        rajinikanth_gray=[None]*limit
j=0
for i in rajini:
    if(j<limit):
        rajinikanth_gray[j]=rgb2gray(rajini_images[j])
        j+=1
    else:
        break
        dhanush_gray=[None]*limit
j=0
for i in dhanush:
    if(j<limit):
        dhanush_gray[j]=rgb2gray(dhanush_images[j])
        j+=1
    else:
        break
        vijay_gray=[None]*limit
j=0
for i in vijay:

    if(j<limit):
        vijay_gray[j]=rgb2gray(vijay_images[j])
        j+=1
    else:
        break
        imshow(rajinikanth_gray[20])
        imshow(vijay_gray[1])
        imshow(dhanush_gray[90])
        rajinikanth_gray[20].shape
        for j in range (100):
    rk=rajinikanth_gray[j]
    rajinikanth_gray[j]=resize(rk,(64,64))
    for j in range (100):
    g=dhanush_gray[j]
    dhanush_gray[j]=resize(g,(64,64))
    for j in range (100):
    k=vijay_gray[j]
    vijay_gray[j]=resize(k,(64,64)
    imshow(rajinikanth_gray[20])
    imshow(vijay_gray[1])
    len_of_images_rajinikanth=len(rajinikanth_gray)
    imshow(dhanush_gray[90])
    image_size_rajinikanth=rajinikanth_gray[1].shape
    image_size_rajinikanth
    flatten_size_rajinikanth=image_size_rajinikanth[0]*image_size_rajinikanth[1]
    for i in range(len_of_images_rajinikanth):
    rajinikanth_gray[i]=np.ndarray.flatten(rajinikanth_gray[i]).reshape(flatten_size_rajinikanth,1)
    rajinikanth_gray=np.dstack(rajinikanth_gray)
    rajinikanth_gray=np.rollaxis(rajinikanth_gray,axis=2,start=0)
    rajinikanth_gray=rajinikanth_gray.reshape(len_of_images_rajinikanth,flatten_size_rajinikanth)
    rajini_data=pd.DataFrame(rajinikanth_gray)
    rajini_data
    rajini_data["label"]="rajinikanth"
    rajini_data
    len_of_images_dhanush=len(dhanush_gray)
    image_size_dhanush=dhanush_gray[1].shape
    flatten_size_dhanush=image_size_dhanush[0]*image_size_dhanush[1]
    flatten_size_dhanush
    
for i in range(len_of_images_dhanush):
    dhanush_gray[i]=np.ndarray.flatten(dhanush_gray[i]).reshape(flatten_size_dhanush,1)
    dhanush_gray=np.dstack(dhanush_gray)
    dhanush_gray=np.rollaxis(dhanush_gray,axis=2,start=0)
    dhanush_gray=dhanush_gray.reshape(len_of_images_d
    hanush,flatten_size_dhanush)

dhanush_gray.shape
dhanush_data=pd.DataFrame(dhanush_gray)

dhanush_data["label"]="dhanush"
dhanush_data
len_of_images_vijay=len(vijay_gray)
image_size_vijay=vijay_gray[1].shape
flatten_size_vijay=image_size_vijay[0]*image_size_vijay[1]
flatten_size_vijay
for i in range(len_of_images_vijay):
    vijay_gray[i]=np.ndarray.flatten(vijay_gray[i]).reshape(flatten_size_vijay,1)
    for i in range(len_of_images_vijay):
    vijay_gray[i]=np.ndarray.flatten(vijay_gray[i]).reshape(flatten_size_vijay,1)
    vijay_gray=np.rollaxis(vijay_gray,axis=2,start=0)
    vijay_gray=vijay_gray.reshape(len_of_images_vijay,flatten_size_vijay)
    vijay_gray.shape
    vijay_data=pd.DataFrame(vijay_gray)
    vijay_data
    vijay_data["label"]="vijay"
    actor_1=pd.concat([rajini_data,dhanush_data])
    actor=pd.concat([actor_1,vijay_data])
    actor
    from sklearn.utils import shuffle
    kollywood_indexed=shuffle(actor).reset_index()
    kollywood_indexed
    kollywood_actors=kollywood_indexed.drop(['index'],axis=1)
    kollywood_actors
