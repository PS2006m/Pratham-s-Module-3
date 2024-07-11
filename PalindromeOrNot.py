'''
Write a Python function that checks whether a passed string is
palindrome or not
'''
s="HeH"
reverse=""
for i in s[::-1]:
    reverse=reverse+i
if reverse==s:
    print("palindrome")
else:
    print("not palindrome")
