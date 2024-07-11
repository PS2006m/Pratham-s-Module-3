'''
Write a Python program to convert a list of tuples into a dictionary
'''

a=[(1,2),(4,5),(7,8)]
b={key: value for key, value in a}
print(b)
