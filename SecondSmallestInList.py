'''
 Write a Python program to find the second smallest number in a list.
'''
list1=[89,31,4,20,1,34,56,90,23,9,11,24,102]
smallest=list1[0]
for i in list1:
    if i<=smallest:
        smallest=i
secondSmallest=list1[list1.index(smallest)+1]
for i in list1:
    if i==smallest:
        continue
    if i<=secondSmallest:
        secondSmallest=i
print("Second smallest number is : ",secondSmallest)
