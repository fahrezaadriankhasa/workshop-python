#!/usr/bin/env python
# coding: utf-8

# In[1]:


squares = [1, 4, 9, 16, 25]
squares


# In[2]:


squares[0]  # indexing returns the item


# In[3]:


squares[-1]


# In[4]:


squares[-3:]  # slicing returns a new list


# In[6]:


squares[:]


# In[7]:


squares + [36, 49, 64, 81, 100]


# In[8]:


cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!


# In[9]:


cubes[3] = 64  # replace the wrong value
cubes


# In[10]:


cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes


# In[11]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters


# In[12]:


# replace some values
letters[2:5] = ['C', 'D', 'E']
letters


# In[13]:


# now remove them
letters[2:5] = []
letters


# In[14]:


# clear the list by replacing all the elements with an empty list
letters[:] = []
letters


# In[15]:


letters = ['a', 'b', 'c', 'd']
len(letters)


# In[17]:


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x


# In[18]:


x[0]


# In[19]:


x[0][1]


# In[ ]:




