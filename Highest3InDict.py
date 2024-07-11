'''
Write a Python program to find the highest 3 values in a dictionary
'''
a={1:15,2:20,3:25,4:30,5:35,6:40,7:45,8:50,9:55}
b=list(a.values())
sort=sorted(b,reverse=True)
highestThree=sort[:3]
print(highestThree)
