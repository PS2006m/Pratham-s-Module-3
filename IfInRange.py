'''
Write a Python function to check whether a number is in a given range
'''
rangeofnos=[]
for i in range(1,51):
    rangeofnos.append(i)
n=int(input("Enter a number "))
if n in rangeofnos:
    print("In range")
else:
    print("Not in range")
