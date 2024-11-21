#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 6
#Reverse a number using while loop


# In[1]:


number = int(input("Enter a number: "))
reversed_number = 0
while number>0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
print("The reversed Number is: ",reversed_number)


# In[ ]:




