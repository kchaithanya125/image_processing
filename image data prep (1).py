#!/usr/bin/env python
# coding: utf-8

# # Recognition of Tamil Actors using PCA and SVM

# # A1-Import system Libraries

# In[3]:


import os
import warnings
warnings.simplefilter('ignore')


# **Import the required system libraries**
# 
# * We need to import ***os module(operating system)***  
# * os module will be used to interact with Operating system
# * In this case we need to upload the images located in our system
# 
# 
# * We need to import the ***warning module*** to ignore all the warnings
# 
# 

# # A2-Import the DataHandling Libraries
# ### 1. Numpy
# ### 2. Pandas

# In[4]:


import numpy as np
import pandas as pd


# * **Numpy**: Library is used for ***Numerical Computation***
# * **NOTE**: Numpy mainly handles data in the form of **arrays**
# * Best part of Numpy is ndarray(**n-dimensional array**)
# * **Pandas**:Library is used for handling ***dataframes***
# * **Note**:Pandas is used to structure the data properly with **proper indices**
# * It is a **datamanipulation library**
# 
# 

# # A3-Import Datavisualization Library
# ### Matplotlib

# In[5]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# * **Matplotlib**:Library is used for ***Data visualization***
# * **Note**: Some of the other ***datavisualization*** libraries in python are
#             *Bokeh
#             *Plotly
#             *Seaborn
#             *geoplotlib
#             *pygal

# # A4- Import required compnents <br>from image processing library
# * ***scikit-image*** is our ***image processing*** library
# * we need to import following functions
#              * imread
#              * imshow
#              * resize
#              * rgb2gray
#              

# In[6]:


from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.color import rgb2gray


# # B1-Setting working directory

# In[7]:


rajini=os.listdir(r"C:\Users\students\Desktop\Images_srm\Images_srm\rajinikanth")


# * **os.listdir** is a command used to get the ***list of elements in a directory***
# * In the above cell we are trying to create a list rajini which has the images<br>present in the folder rajinikanth
# * These images are located in the folder rajinikanth in the system
# * we can access this folder by os.listdir
# * Now rajini is a list of ***100 images***
# * Now vijay is a list of ***100 images***
# * Now dhanush is a list of ***100 images***

# In[8]:


vijay=os.listdir(r"C:\Users\students\Desktop\Images_srm\Images_srm\vijay")


# In[13]:


dhanush=os.listdir(r"C:\Users\students\Desktop\Images_srm\Images_srm\dhanush")


# # B2-Reading Image as a matrix of numbers

# In[12]:


limit=100
rajini_images=[None]*limit
j=0
for i in rajini:
    if(j<limit):
        rajini_images[j]=imread(r"C:\Users\students\Desktop\Images_srm\Images_srm\rajinikanth/"+i)
        j+=1
    else:
        break


# **imread()**
# * ***imread*** command in ***scikitimage*** is used load an image
# * This command returns a ***nd-array***
# * It returns ***pixel values*** (intensity)
# * An RGB-image returns Rows**x**Columns**x**colour band

# In[19]:


vijay_images=[None]*limit
j=0
for i in vijay:
    if(j<limit):
        vijay_images[j]=imread(r"C:\Users\students\Desktop\Images_srm\Images_srm\vijay/"+i)
        j+=1
    else:
        break


# In[20]:


dhanush_images=[None]*limit
j=0
for i in dhanush:
    if(j<limit):
        dhanush_images[j]=imread(r"C:\Users\students\Desktop\Images_srm\Images_srm\dhanush/"+i)
        j+=1
    else:
        break


# ### B2.1- View the images

# **imshow()**
# * The input will be ***ndarray*** or image file
# * This command ***displays an image***

# In[21]:


imshow(rajini_images[1])


# In[22]:


imshow(dhanush_images[1])


# In[23]:


imshow(vijay_images[10])


# # B3-Convert Color images to Gray scale Images
# **rgb2gray**
# * This command converts an image with ***rgb image*** to ***gray image***
# * rgb means ***red blue green***

# In[24]:


rajinikanth_gray=[None]*limit
j=0
for i in rajini:
    if(j<limit):
        rajinikanth_gray[j]=rgb2gray(rajini_images[j])
        j+=1
    else:
        break


# Let us understand the step by step code of converting colour 2 gray
# * Step:1-Create a ***list of None***
# * The ***len of the list*** should be ***equal to no of images***
# * Initiate a ***for loop*** which starts from 0 to len of the images
# * Now write a ***conditional statement*** which checks is j less than len of images
# * if its is less then assign that number as an index to previously created list
# * Convert the current indexed image to gray scale using ***rgb2gray*** command
# * Increase the j variable by one so the next image follows the process

# In[25]:


dhanush_gray=[None]*limit
j=0
for i in dhanush:
    if(j<limit):
        dhanush_gray[j]=rgb2gray(dhanush_images[j])
        j+=1
    else:
        break


# In[26]:


vijay_gray=[None]*limit
j=0
for i in vijay:
    if(j<limit):
        vijay_gray[j]=rgb2gray(vijay_images[j])
        j+=1
    else:
        break


# ### B3.2-View the gray scale Images

# In[27]:


imshow(rajinikanth_gray[20])


# In[28]:


imshow(vijay_gray[1])


# In[29]:


imshow(dhanush_gray[90])


# ### B4.0-Check the image matrix size before resizing
# 
# ***Check the shape of each image using .shape function***
# * The images we have selected are in ***different sizes***

# In[30]:


rajinikanth_gray[20].shape


# In[31]:


rajinikanth_gray[23].shape


# In[32]:


rajinikanth_gray[93].shape


# In[33]:


rajinikanth_gray[53].shape


# ### B4.1-Matrix Resizing
# We need to resize them to a ***standard resolution***
# * For the given dataset ***512x512*** is looking good
# * So let's resize the ***image*** using ***resize()*** command

# In[34]:


for j in range (100):
    rk=rajinikanth_gray[j]
    rajinikanth_gray[j]=resize(rk,(64,64))


# **resize()**
# * The resize command takes the image and the size as inputs

# In[35]:


for j in range (100):
    g=dhanush_gray[j]
    dhanush_gray[j]=resize(g,(64,64))


# In[36]:


for j in range (100):
    k=vijay_gray[j]
    vijay_gray[j]=resize(k,(64,64))


# ### B4.2-View the resized images

# In[37]:


imshow(rajinikanth_gray[20])


# In[38]:


rajinikanth_gray[20].shape


# In[39]:


imshow(vijay_gray[1])


# In[40]:


imshow(dhanush_gray[90])


# # B6-Image matrix to vector conversion
# In this step we need to convert the image which is in matrix form to vector
# 
# 

# ### Step B6.0: Find out the number of ***gray_scale images***

# In[41]:


len_of_images_rajinikanth=len(rajinikanth_gray)


# ### Step B6.1: Create a variable **image_size_rajinikanth**
# 

# * step3: This variable should have the size of the image
# * Output of this variable will be ***(512,512)***

# In[42]:


image_size_rajinikanth=rajinikanth_gray[1].shape


# In[43]:


image_size_rajinikanth


# ### Step B6.2: Create a variable ***flatten_size_rajinikanth*** which contains the product of (512,512)
# 

# In[44]:


flatten_size_rajinikanth=image_size_rajinikanth[0]*image_size_rajinikanth[1]


# In[45]:


flatten_size_rajinikanth


# ### Step B6.3:Now ***flatten the image from (512,512) matrix to 266144,1 vector***

# In[46]:


for i in range(len_of_images_rajinikanth):
    rajinikanth_gray[i]=np.ndarray.flatten(rajinikanth_gray[i]).reshape(flatten_size_rajinikanth,1)


# **np.ndarray.flatten**
# 
# This function is used to convert the image from (512,512) matrix to 266144 elements vector
# 

# ### Step B6.4: Now Stack the individual image array elements into one array
#     This process is called stacking
#     We use the function np.dstack

# In[47]:


rajinikanth_gray=np.dstack(rajinikanth_gray)


# **np.dstack**
# * This will help us to **stack all the arrays** or vectors togather
# * This operation is equivalent to ***concantenation***
# * In the current operation we have ***100 images which are vectorized***
# * Now we are stacking all the vectors or arrays into one ***ndarray***
# * ***A list will be converted into an array***

# ### Step B6.5: Now if needed change the axis of the array elements
# * In general when we work with images, we consider the array <br> to have a shape of rowxcolumnxcolour_channel
# * But currently it is columnxcolour_channelxrow
# * To change this we need to use the np.rollaxis function

# In[48]:


rajinikanth_gray=np.rollaxis(rajinikanth_gray,axis=2,start=0)


# In[49]:


rajinikanth_gray.shape


# **np.rollaxis**
# This command is used to move the position of an axis in the ndarray
# * Currently we need to bring the data in axis 2 to axis 0

# ### Step B6.6: 

# In[50]:


rajinikanth_gray=rajinikanth_gray.reshape(len_of_images_rajinikanth,flatten_size_rajinikanth)


# In[51]:


rajinikanth_gray.shape


# ### B7-Creating a Dataframe of the image Vectors
# * Now we need to convert our ***ndarray*** to ***Dataframe***
# * ***A dataframe has proper indexing***
# * To manipulate data and its positions, this helps us a lot
# * For this operation we need to use ***PANDAS library***
# * In our initial steps we have imported our ***PANDAS library as pd***
# * We need to use the function ***pd.DataFrame***

# In[52]:


rajini_data=pd.DataFrame(rajinikanth_gray)


# **pd.DataFrame()**
# * ***Pd.Dataframe*** is used to create a dataframe
# * The input should be a ***ndarray*** name

# ### Type the image dataframe name to look into the dataframe

# In[54]:


rajini_data


# ### B8-Labelling the rows of the Dataframe
# * Here since it is supervised learning, we need to label the images
# * We need to tell the system that this image or data belongs to rajinikanth
# * For this we need to create a new column named Label with the label name

# In[44]:


rajini_data["label"]="rajinikanth"


# ### Now check the dataframe again

# In[55]:


rajini_data


# ### Rinse and Repeat the same for dhanush and vijay

# ## Follow B1-B8 steps for dhanush

# In[56]:


len_of_images_dhanush=len(dhanush_gray)


# In[57]:


image_size_dhanush=dhanush_gray[1].shape


# In[58]:


flatten_size_dhanush=image_size_dhanush[0]*image_size_dhanush[1]


# In[59]:


flatten_size_dhanush


# In[60]:



for i in range(len_of_images_dhanush):
    dhanush_gray[i]=np.ndarray.flatten(dhanush_gray[i]).reshape(flatten_size_dhanush,1)


# In[61]:


dhanush_gray=np.dstack(dhanush_gray)


# In[62]:


dhanush_gray=np.rollaxis(dhanush_gray,axis=2,start=0)


# In[63]:


dhanush_gray=dhanush_gray.reshape(len_of_images_dhanush,flatten_size_dhanush)


# In[64]:


dhanush_gray.shape


# In[65]:


dhanush_data=pd.DataFrame(dhanush_gray)


# In[66]:


dhanush_data


# In[67]:


dhanush_data["label"]="dhanush"


# In[68]:


dhanush_data


# ## Follow B1-B8 steps for vijay

# In[69]:


len_of_images_vijay=len(vijay_gray)


# In[70]:


image_size_vijay=vijay_gray[1].shape


# In[71]:


flatten_size_vijay=image_size_vijay[0]*image_size_vijay[1]


# In[72]:



flatten_size_vijay


# In[73]:


for i in range(len_of_images_vijay):
    vijay_gray[i]=np.ndarray.flatten(vijay_gray[i]).reshape(flatten_size_vijay,1)


# In[74]:


vijay_gray=np.dstack(vijay_gray)


# In[75]:


vijay_gray=np.rollaxis(vijay_gray,axis=2,start=0)


# In[76]:


vijay_gray=vijay_gray.reshape(len_of_images_vijay,flatten_size_vijay)


# In[77]:


vijay_gray.shape


# In[78]:


vijay_data=pd.DataFrame(vijay_gray)


# In[79]:


vijay_data


# In[80]:


vijay_data["label"]="vijay"


# In[81]:


vijay_data


# In[83]:


actor_1=pd.concat([rajini_data,dhanush_data])


# In[85]:


actor=pd.concat([actor_1,vijay_data])


# In[86]:


actor


# In[87]:


from sklearn.utils import shuffle


# In[89]:


kollywood_indexed=shuffle(actor).reset_index()


# In[90]:


kollywood_indexed


# In[93]:


kollywood_actors=kollywood_indexed.drop(['index'],axis=1)


# In[94]:


kollywood_actors


# In[ ]:


kollywood_actors.to_csv()

