#!/usr/bin/env python
# coding: utf-8

# In[1]:


class stack:
    def __init__(self,size):
        self.data = [0 for i in range(size)]
        self.top = 0
        self.size = size
    
    def isEmpty(self):
        return self.top == 0
    
    def push(self,val):
        if self.top != self.size:
            self.data[self.top] = val
            self.top += 1
        else:
            return "stack overflow"
        
    def pop(self):
        if not self.isEmpty():
            x = self.data[self.top-1]
            self.top -= 1
            return x
        else:
            return "stack underflow"
        
    def peek(self):
        if not self.isEmpty():
            return self.data[self.top-1]
        
    def count(self):
        return self.top
        
class Queue:
    def __init__(self,size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.rare = 0
        self.front = 0
        self.count = 0
        
    def isEmpty(self):
        if self.count == 0:
            return True
        return False
        
    def enqueue(self,val):
        if self.count != self.size:
            self.data[self.rare] = val
            self.rare = (self.rare + 1) % self.size
            self.count += 1
        else:
            return "Queue Overflow"
    
    def dequeue(self):
        if self.count != 0:
            x = self.data[self.front]
            self.front = (self.front + 1) % self.size
            self.count -= 1
            return x
        else:
            return "Queue Underflow"
        
    def peek(self):
        if not self.isEmpty():
            return self.data[self.rare]
        return "Queue is empty"
    
    def Count(self):
        return self.count


# In[ ]:




