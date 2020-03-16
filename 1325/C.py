#!/usr/bin/env python
# coding: utf-8

# In[83]:


n = int(input())
edges = []
degrees = [0]
for i in range(n):
    degrees.append(0)


# In[84]:


output = []
for i in range(n-1):
    output.append(-1)
    


# In[85]:


def d3():
    d3_vertex = 0
    for i in range(n+1):
        if ( degrees[i] > 2 ):
            d3_vertex = i
    return d3_vertex


# In[86]:


for i in range (n-1):
    inp = input().split()
    inp = [int(i) for i in inp]
    
    inp.sort()
    edges.append(inp)
    
    degrees[inp[0]]= degrees[inp[0]] +1
    degrees[inp[1]]= degrees[inp[1]] +1


# In[91]:


f = d3()
if (f > 0):
    u = 0;
    for i in range(n-1):
        if(edges[i][0]==f or edges[i][1]==f):
            output[i] = u
            u = u+1
            
    for i in range(n-1):
        if(output[i]==-1):
            output[i] = u
            u = u+1     
            
    for i in range(n-1):
        print(output[i])
    
else:
    for i in range(n-1):
        print(i)


# In[ ]:




