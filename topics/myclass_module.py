#!/usr/bin/env python
# coding: utf-8

# In[1]:


#function

def world():
    print("Hello, World!")

#variable
shark = "Sammmy"


#class

class Octopus:
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def about_the_octopus(self):
        print("This octopus is " + self.color + ".")
        print(self.name + " is the octopus's name.")

