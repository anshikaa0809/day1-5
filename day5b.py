#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=[1,2,3,4,5,6,7]
while a:
    b=a.pop()
    print(f"popped element:{b}")
    print(a)


# In[5]:


set1=set("hello")
set2=set("peoplezzzz")
set1.union(set2)


# In[6]:


set1=set("hello")
set2=set("peoplezzzz")
set1.intersection(set2)


# In[16]:


set={1,2,3,4,5,6,7,8}
set.update([9])
print(set)


# In[23]:


set={1,2,3,4,5,6,7,8}
set.remove(4)
print(set)


# In[22]:


set={1,2,3,4,5,6,7,8}
set.discard(10)
print(set)


# In[28]:


set={1,2,3,4,5,6,7,8}
set.pop()
print(set)
set.pop()
print(set)


# In[30]:


set={1,2,3,4,5,6,7,8}
set.clear()
print(set)


# In[37]:


set1={1,2,3,4,5}
set2={5,6,7,8,9}
set1.difference(set2)


# In[39]:


set1={1,2,3,4,5}
set2={5,6,7,8,9}
set2.issubset(set1)


# In[41]:


set1={1,2,3,4,5}
set2={5,2}
set1.issuperset(set2)


# In[ ]:





# In[ ]:




