'''
Write a Python function that takes a list and returns a new list with unique
elements of the first list.
'''
def removeDuplicates(list1):
    tempList = []
    list2 = []
    for i in list1:
        if i not in tempList:
            tempList.append(i)
            list2.append(i)
    return list2
list1 = [1, 2, 2, 3, 4, 4, 5, 1, 6]
list2 = remove_duplicates(input_list)
print("Original list is ")
print(list1)
print("List with unique elements is ")
print(list2)
