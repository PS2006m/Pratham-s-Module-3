'''
Write a Python script to check if a given key already exists in a
dictionary.
'''
a={1:'a',2:'b',3:'c',4:'d',5:'e'}
b=3
for i in a:
    if i==b:
        print("Exists")
        break
else:
    print("Doesn't Exists")
