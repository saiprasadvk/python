#!/usr/bin/env python
# coding: utf-8

# In[26]:


class cals():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
    def sub(self):
        print(self.a-self.b)
    
def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    obj=cals(a,b)
    obj.sub()
            
if __name__ == "__main__":
    main()

