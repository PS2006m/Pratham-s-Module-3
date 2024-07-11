'''
Write a Python script to print a dictionary where the keys are numbers
between 1 and 15.
'''
a={1:'a',20:'b',9:'c',4:'d',16:'e'}
b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in a:
    if i in b:
        print(a.get(i))
