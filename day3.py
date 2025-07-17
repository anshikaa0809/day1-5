#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    n=input("enter letter")
    if n=='q':
        print("exited")
        break
    else:
        print("you typed:",n)


# In[2]:


password="hey123"
at=2
while at>0:
    n=input("password")
    if n==password:
        print("access granted😴")
        break
    else:
        print(f"wrong password:!{at}attempts left")
    
        


# In[3]:


i=1
while i<100:
    if i%7==0:
        print(f"{i}divisible")
    else:
        print(f"{i}not divisible")
    i+=1
        


# In[4]:


password="hey123"
for i in range(0,3):
     n=input("password")
     if n==password:
         print("access granted😴")
         break
     else:
         print(f"wrong password:!{2-i}attempts left")
    


# In[5]:


for i in range(1,7):
    if i==4:
        continue
    print(i)


# In[6]:


for i in range(1,11):
    if i==5:
        continue
    if i==8:
        break
    print(i)


# In[7]:


for i in range(0,5):
    n=input("password")
if n=="forget":
    continue
elif n=="anshu":
    print("okk")
    break
else:
    i-=1
    print(f"{4-i}attempts left")


# In[13]:


str="python"
i=len(str)
for i in range(1,7):
    if i==5:
        continue
    if i==6:
        break
    print(str)


# In[19]:


word = "PYTHONPROGRAMMING"
for letter in word:
    if letter == 'O':
        continue  
    if letter == 'N':
        print("😎 Breaking at 'N'")
        break     
    print(" Letter:", letter)


# In[23]:


def sum():
    a=2
    b=5
    sum=a+b
    print("sum is",sum)
    sum()


# In[ ]:




