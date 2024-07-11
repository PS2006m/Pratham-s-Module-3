'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd
'''
from itertools import product
data={'1': ['a', 'b'], '2': ['c', 'd']}
keys = sorted(data.keys())  # Sorting keys to ensure consistent output order
combinations = product(*(data[key] for key in keys))
result = [''.join(combination) for combination in combinations]
print(result)
