#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 5
#Find the factorial of a given number using loops


# In[1]:


Number = int(input("Enter the number: "))
factorial = 1
for i in range(1,Number+1):
    factorial = factorial * i
print("Factorial of the number", Number, "is" ,factorial)


# In[ ]:




