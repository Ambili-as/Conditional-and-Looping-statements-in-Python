#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 8 
#Write a program to print the inputted value as it is and 
#break the loop if the value is 'done'. 


# In[2]:


while True:
    user_input = input("Enter a value (type 'done' to exit): ")
    if user_input == 'done':
        break
    print(user_input)


# In[ ]:




