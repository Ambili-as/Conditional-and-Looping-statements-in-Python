#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 2
#A certain cinema currently sells tickets for a full price of 6 pounds, 
#but always sells tickets for half price to people who are less than 16 years old, 
#and for a third of the price for people who are 60 years old or more.


# In[6]:


Age = int(input("Enter your Age: "))
Full_price = 6.00
if Age<16:
    Ticket_price = Full_price/2
elif Age>60:
    Ticket_price = Full_price/3
else:
    Ticket_price = Full_price
print("Your Ticket costs £",Ticket_price)


# In[ ]:





# In[ ]:




