'''
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
'''
a=["Hello","Web","Day","Door","Load","Hello"]
flag=False
for i in a:
    if len(i)<2:
        flag=True
        break
if flag:
    print("One of the strings has less than 2 lengths")
else:
    count=0
    for i in a:
        count+=1
    print("Number of Strings are ",count)
    if a[0] is a[-1]:
        print("First and Last Strings are equal")
    else:
        print("First and Last Strings are not equal")
