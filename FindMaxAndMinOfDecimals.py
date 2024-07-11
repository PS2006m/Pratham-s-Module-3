'''
 Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers.
'''
n=int(input("Enter amount you wish to input "))
y=[]
for i in range(0,n):
    number=int(input("Enter a number "))
    y.append(number)
maxnum=max(y)
minnum=min(y)
print("Max is ",maxnum)
print("Min is ",minnum)
