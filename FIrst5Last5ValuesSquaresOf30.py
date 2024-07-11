'''
Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
'''
list1=[1,2,3,25,16,9,4,90,100,30,22,112,140,200,81,144,100]
list2=[]
print("List is")
print(list1)
for i in list1[:5]:
    for j in range(1,30):
        j=j*j
        if i==j:
            list2.append(i)
for i in list1[-1:-6:-1]:
    for j in range(1,30):
        j=j*j
        if i==j:
            list2.append(i)
print("Required List")
print(list2)
            
