#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 10 

#Write a program to print the following pattern: 
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1


# In[1]:


n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end = " ")
    print()


# In[ ]:




