#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


import numpy as np
import pandas as pd
import scipy.io as sio

#%matplotlib inline 


# In[26]:


uni1vmag=sio.loadmat('../../washmc-data/uni4/hhzverustime.mat')


# In[29]:


#print(uni1vmag)


# In[30]:


print(uni1vmag['evelv1Mm'].shape)
block=uni1vmag['evelvp5Mm']
xvals=np.linspace(start=1, stop=303, num=303)
slice=block[62][62][1:304]


# In[11]:


#print(uni1vmag)


# In[32]:


block=uni1vmag['evelvp5Mm']

ax1 = plt.subplot(131)
ax1.margins(0.0)           # Default margin is 0.05, value 0 means fit
ax1.plot(xvals, block[62][62][1:304])
ax1.set_title('0.5Mm')

block=uni1vmag['evelv1Mm']

ax2 = plt.subplot(132)
ax2.margins(x=0)   # Values in (-0.5, 0.0) zooms in to center
ax2.plot(xvals, block[62][62][1:304])
ax2.set_title('1Mm')

block=uni1vmag['evelv2Mm']

ax3 = plt.subplot(133)
ax3.margins(x=0)   # Values in (-0.5, 0.0) zooms in to center
ax3.plot(xvals, block[62][62][1:304])
#plt.imshow(block[62][:][1:304].T)
ax3.set_title('2Mm')

plt.show()


# In[ ]:




