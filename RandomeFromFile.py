'''
Write a Python program to read a random line from a file.
'''
import random
with open("randomeFile.txt", "w") as filename:
    for i in range(1, 11):
        filename.write(str(i) + "\n")
with open("randomeFile.txt", "r") as file:
    lines = file.readlines()
    num_lines = len(lines)
    random_line_num = random.randint(0, num_lines - 1)
    random_line = lines[random_line_num].strip()
print("Random line from the file:")
print(random_line)
