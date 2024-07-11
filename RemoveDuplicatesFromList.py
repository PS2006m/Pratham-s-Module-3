'''
Write a Python program to remove duplicates from a list
'''
list1 = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Original list is ")
print(list1)
for i in list1[0:]:
    for j in list1[list1.index(i)+1:]:
        if i==j:
            list1.remove(j)
print("List after removing duplicates")
print(list1)
