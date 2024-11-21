#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 7 
#Finding the multiples of a number using loop


# In[6]:


number = int(input("Enter the number: "))
count = int(input("No. of multiples to find : "))
print(count, "Multiples of", number, ": ")
for i in range(1, count+1):
    multiple = number * i
    print(multiple)
        
        


# In[ ]:




