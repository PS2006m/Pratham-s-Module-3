'''
Write a Python function that takes two lists and returns true if they have
at least one common member.
'''
def ifCommonOrNot(list1,list2):
    for i in list1:
        for  j in list2:
            if i==j:
                return True
    return False

list1=[1,2,3,4,5,6]
list2=[11,10,9,8,7,6]
print(list1)
print(list2)
flag=ifCommonOrNot(list1,list2)
print(flag)
list2.pop()
print(list1)
print(list2)
flag=ifCommonOrNot(list1,list2)
print(flag)
