'''
Write a Python program to returns sum of all divisors of a number
'''
n = int(input("Enter a number: "))
divisors_sum = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisors_sum += i
print("Sum of divisors is ",divisors_sum)
