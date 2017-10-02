
# coding: utf-8

# In[9]:


for a in range(5,0,-1):
    for i in range(a//2+1):
        print(" ",end="")
    for j in range(6-a):
        print(" *",end="")
    print()

