'''
Write a Python function to get the largest number, smallest num and sum
of all from a list.
'''
a=[12,34,19,76,45,33,20,10,4]
i=a[0]
for j in a:
    if j>i:
        i=j
largest=i
i=a[0]
for j in a:
    if j<i:
        i=j
smallest=i
sum=0
for i in a:
    sum=sum+i
print("Largest is ",largest)
print("Smallest is ",smallest)
print("Sum is ",sum)

