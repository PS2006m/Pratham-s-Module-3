'''
Write a Python program to replace last value of tuples in a list.
'''
a=[(1,2),(3,4,5),(6,7)]
b=[]
for i in a:
    if isinstance(i,tuple) and len(a)>0:
         c = i[:-1] + (0,)
         b.append(c)
print(b)
        
