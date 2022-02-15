#!/usr/bin/env python
# coding: utf-8

# In[1]:


'spam eggs'  # single quotes


# In[2]:


'doesn\'t'  # use \' to escape the single quote...


# In[3]:


"doesn't"  # ...or use double quotes instead


# In[4]:


'"Yes," they said.'


# In[5]:


"\"Yes,\" they said."


# In[6]:


'"Isn\'t," they said.'


# In[7]:


'"Isn\'t," they said.'


# In[8]:


print('"Isn\'t," they said.')


# In[9]:


s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output


# In[10]:


print(s)  # with print(), \n produces a new line


# In[11]:


print('C:\some\name')  # here \n means newline!


# In[12]:


print(r'C:\some\name')  # note the r before the quote


# In[14]:


print("""Usage: thingy [OPTIONS]
      -h                        Display this usage message
      -H hostname               Hostname to connect to
""")


# In[16]:


# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'


# In[17]:


'Py' 'thon'


# In[18]:


text = ('Put several strings within parentheses '
        'to have them joined together.')
text


# In[19]:


prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal


# In[20]:


('un' * 3) 'ium'


# In[21]:


prefix + 'thon'


# In[22]:


word = 'Python'
word[0]  # character in position 0


# In[23]:


word[5]  # character in position 5


# In[24]:


word[-1]  # last character


# In[25]:


word[-2]  # second-last character


# In[26]:


word[-6]


# In[27]:


word[0:2]  # characters from position 0 (included) to 2 (excluded)


# In[28]:


word[2:5]  # characters from position 2 (included) to 5 (excluded)


# In[29]:


word[:2]   # character from the beginning to position 2 (excluded)


# In[30]:


word[4:]   # characters from position 4 (included) to the end


# In[31]:


word[-2:]  # characters from the second-last (included) to the end


# In[32]:


word[:2] + word[2:]


# In[33]:


word[:4] + word[4:]


# In[34]:


word[42]  # the word only has 6 characters


# In[35]:


word[4:42]


# In[36]:


word[42:]


# In[37]:


word[0] = 'J'


# In[38]:


word[2:] = 'py'


# In[39]:


'J' + word[1:]


# In[40]:


word[:2] + 'py'


# In[41]:


s = 'supercalifragilisticexpialidocious'
len(s)


# In[ ]:




