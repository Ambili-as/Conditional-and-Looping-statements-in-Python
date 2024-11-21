#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 3 
#Name your file: BodyMassIndex.py 
#Write a program to calculate your BMI and give weight status. 
#Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.
#The metric BMI formula accepts weight in kilograms and height in meters: 
#BMI= weight(kg)/height2(m2) 
#BMI Weight Status Categories table 
#BMI range - kg/m2 Category 
#Below 18.5 Underweight 
#18.5 -24.9 Normal 
#25 - 29.9 Overweight 
#30 & Above Obese 


# In[4]:


weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
BMI = weight / (height **2)
if BMI<18.5:
    status = "Underweight"
elif 18.5<=BMI<=24.9:
    status = "Normal"
elif 25<=BMI<=29.9:
    status = "Overweight"
else:
    status = "Obese"
print("Your BMI is",BMI)
print("You are in the",status,"Range")


# In[ ]:




