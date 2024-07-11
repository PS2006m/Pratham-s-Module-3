'''
Write a Python script to concatenate following dictionaries to create a
new one.
'''
a=[{1:1},{2:2},{3:3},{4:4}]
c={}
for i in a:
    c.update(i)
print(c)
