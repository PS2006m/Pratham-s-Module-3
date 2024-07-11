'''
Write a Python script to sort (ascending and descending) a dictionary by
value
'''
a={1:1,4:4,3:3,6:6,5:5}
b=[]
for i in a:
    b.append(a.get(i))
b.sort()
print(b)
a.clear()
for i in b:
    c={i:i}
    a.update(c)
print(a)
