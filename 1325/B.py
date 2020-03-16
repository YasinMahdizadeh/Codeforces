#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input())
arrays = []
for i in range(n):
    x = int(input())
    a = []
    a = input().split()
    a = [int(i) for i in a]
    arrays.append(a)
    


# In[10]:


for i in range(n):
    a = []
    a = set(arrays[i])
    print(len(a))


# In[ ]:




