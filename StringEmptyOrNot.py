'''
Write a Python program to check a list is empty or not
'''
lists=[1,2,3]
print(lists)
try:
    a=lists[0]
    print("List is not empty")
except Exception as e:
    print("List is empty")
lists.clear()
print(lists)
try:
    a=lists[0]
    print("List is not empty")
except Exception as e:
    print("List is empty")
