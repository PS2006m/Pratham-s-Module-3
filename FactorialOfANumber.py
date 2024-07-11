'''
Write a Python function to calculate the factorial of a number (a
nonnegative integer)
'''
def factorialOfNumber(n1):
    if n1==0:
        return 1
    else:
        n1=n1*factorialOfNumber(n1-1)
    return n1

while True:
    n=int(input("Enter a number "))
    if n>=0:
        break
    else:
        print("Enter a number above or equal to 0")
factorial=factorialOfNumber(n)
print("Factorial of ",n," is ",factorial)
