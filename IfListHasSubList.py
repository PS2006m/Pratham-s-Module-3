'''
Write a Python program to check whether a list contains a sub list
'''
list1=[1,2,[3,4,5,6],7,8,9,10]
print("List with sublist is")
print(list1)
if list in list1:
    print("Yes")
else:
    print("No")
for i in list1:
    if i==list:
        print("List does have SubList")
        break
else:
    print("List doesn't have SubList")
