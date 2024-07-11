'''
Write a Python program to get unique values from a list
'''
flag=True
mainlist = [1, 2, 3, 4, 5, 6]
sublist = [3, 4, 5]
sublistLength = len(sublist)
for i in range(len(mainlist) - sublistLength + 1):
    if mainlist[i:i + sublistLength] == sublist:
        flag=True
        break
else:
    flag=False
print("Main list:", mainlist)
print("Sublist:", sublist)
print("Main list contains sublist is ", flag)
