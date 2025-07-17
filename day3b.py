#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum():
    a=2
    b=5
    sum=a+b
    print("sum is",sum)
sum()


# In[10]:


for ch in str("hello"):
    print(ch)


# In[18]:


for x in range[1,10,3]:
    print(x)


# In[15]:


if x:
    print('Hello')
    where x=0


# In[20]:


for x in [1,10,3]:
    print(x)


# In[21]:


print("helloworld")


# In[22]:


a=2
b=4
sum=a+b
print(sum)


# In[23]:


a=int(input("enter"))
if a%2==0:
    print("even")
else:
    print("odd")


# In[24]:


a=int(input("enter"))
b=int(input("enter"))
if a>b:
    print("a is greater")
else:
    print("b is greater")


# In[25]:


a=int(input("enter"))
if a>0:
    print("positive")
else:
    print("negetive")



# In[29]:


i=1
while i<11:
      print(i)
      i+=1
        


# In[30]:


num = int(input("Enter number: "))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")


# In[36]:


n=int(input("enter"))
f=1
for i in range(1,n+1):
    f*= i
    print(f)


# In[45]:


def rev(word):
    print(word[::-1])
rev("1234")


# In[46]:


aaa=input("Enter string:")
vowels=0
for i in aaa:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


# In[47]:


a=int(input("enter"))
if a%1==0 and a%a==0:
    print("prime it is")
else:
    print("not prime")


# In[49]:


n = int(input("enter"))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("enter a no.")
elif n == 1:
   print("Fibonacci sequence upto",n)
   print(n1)
else:
   print("Fibonacci:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


# In[53]:


a= [10, 20, 30, 40, 50]
b= sum(a)
print(b)


# In[1]:


def fibo(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
       print("enter a no.")
    elif n == 1:
       print("Fibonacci sequence upto",n)
       print(n1)
    else:
       print("Fibonacci:")
       while count < n:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
fibo(6)


# In[ ]:




