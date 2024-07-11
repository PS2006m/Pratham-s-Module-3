'''
Write a Python program to unzip a list of tuples into individual lists
'''
a=[(1,2,3),(4,5,6),(7,8,9)]
b=[];c=[];d=[]
count=0
for i in a:
    if count==0:
        b.append(i)
    elif count==1:
        c.append(i)
    else:
        d.append(i)
    count+=1
print(b)
print(c)
print(d)
