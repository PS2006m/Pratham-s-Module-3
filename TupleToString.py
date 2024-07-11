'''
Write a Python program to convert a tuple to a string
'''
a=(1,2,3,4)
string=""
for i in a:
    i=str(i)
    string=string+i
print(string)
