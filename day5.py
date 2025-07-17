#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[]
a.insert(0,1)
a.append(2)
a.append(3)
a.append(4)
print(a)


# In[2]:


l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)


# In[4]:


l = [10, 20, 30, 40]
l.insert(2,25)
print(l)


# In[8]:


l = [10, 20, 30, 20, 40]
l.remove(20)
print(l)


# In[10]:


l= [1, 2, 3, 4, 5] 
a=l.pop()
print(a)
print(l)


# In[12]:


l=[5, 10, 15, 20, 25]
l.index(15)


# In[13]:


l=[1, 2, 2, 3, 2, 4, 2]
l.count(2)


# In[18]:


l=[10, 5, 7, 3]
l.sort()
print(l)
l.sort(reverse='true')
print(l)


# In[19]:


l=[1, 2, 3, 4, 5]
l.reverse()
print(l)


# In[23]:


a= [1, 2, 3]
b=a.copy()
b.insert(2,7)
print(b)
print(a)


# In[7]:


a=[1,6,7,5,9,2,4,3,8,10]
a.sort()
print(a)
a.index(10)


# In[12]:


a=[1,2,3,4,5,6,7,8]
b= [num for num in a if num % 2 != 0]
print(b)


# In[14]:


a=['anshika','palak','athira']
b=input("enter")
if b in a:
    a.remove(b)
else:
    print("not found")
print(a)


# In[22]:


a=[1,2,3,4,5,6,7,8]
b=int(input("enter"))
if b in a:
    print( a.index(b))
    a.remove(b)
else:
    print("not found")
print(a)


# In[18]:


a=['cat','ant','elephant','koala','donkey']
a.sort()
print(a)


# In[19]:


a=['python','python','java','C++','python']
a.count('python')


# In[20]:


a= [1, 2, 3]
b=a.copy()
b.insert(2,7)
print(b)
print(a)


# In[29]:


a=[1,2,3,4,5,6,7]
b=int((len(a))/2)
a.insert(b,10)
print(a)


# In[ ]:


a=[1,2,3,4,5,6,7]
while a:
    b=a.pop()
    print(f"popped element:{b}")


# In[ ]:




