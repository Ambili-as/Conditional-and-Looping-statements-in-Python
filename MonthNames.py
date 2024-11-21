#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a program that reads an integer value between 1 and 12 
#from the user and prints output the corresponding month of the year.


# In[4]:


Months = ["January","February","March","April", "May","June","July","August","September","October","November","December" ]


# In[22]:


Month_Number = int((input("Enter a number between 1 and 12: ")))
if 1 <= Month_Number <= 12:
    print("The month is: ",
          Months[Month_Number - 1])
else:
    print("Invalid input! Please enter a number between 1 and 12.")
        


# In[ ]:





# In[ ]:




