#!/usr/bin/env python
# coding: utf-8

# In[28]:


a=46.8
print(int(a))


# In[29]:


a=int(input("enter no"))
print("enter number")
if a<0:
    print("negetive no")
else:
    print("positive no")


# In[5]:


age=int(input("enter no"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible")


# In[6]:


n=int(input("enter no"))
if n%2==0:
    print("even")
else:
    print("odd")


# In[10]:


n=str(input("enter string"))
if len(n)>5:
    print("lengthy")
else:
    print("short")


# In[12]:


n=int(input("enter no"))
if n>=40:
    print("pass")
else:
    print("fail")


# In[25]:


winters=["jan","feb","mar"]
summers=['april','may','june']
monsoon=['july','aug','sep']
prewinter=['nov','dec','oct'];
month=str(input("enter"))
if month==winters:
    print("winter")
elif month==summers:
    print("summers")
elif month==monsoon:
    print("rainy")
else:
    print("pre winters")


# In[33]:


age_of_car=int(input("enter"))
if age_of_car<15:
    print("still good")
else:
    print("expired")


# In[34]:


x = 4
y = 2
if x > 2:
    if y > 3:
        print('Yes')
    else:
        print('No')


# In[40]:


g=int(input("enter"))
if g>90:
    print("A")
elif g>75:
    print("B")
elif g>60:
    print("C")
else:
    print("D")


# In[39]:


a=int(input("enter"))
if a%2==0:
    print("even")
    if a>10:
        print("it is greater than 10")
else:
    print("odd")
        


# In[41]:


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a>b and a>c:
        print("A is greatest")
elif b>a and b>c:
        print("b is greatest")
else:
        print("c is greatest")


# In[43]:


a = 0
while (a < 3):
    a = a + 1
    print("Hello peopllzzz")


# In[ ]:




