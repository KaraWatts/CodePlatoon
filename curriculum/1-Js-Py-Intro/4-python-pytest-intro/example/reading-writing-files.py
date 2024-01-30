"""
reading-writing-files.py

To be used with the intro-to-python lesson when teaching reading/writing files.
example.txt should be located in the same dir
"""
import os # not needed for relative path imports

# Reading a file using the relative path
with open('./example.txt', 'r') as file:
    for line in file:
        print(line)

# Reading a file using the absolute path
abs_path = os.path.abspath('./example.txt')
print(abs_path)

with open(abs_path, 'r') as file:
    for line in file:
        print(line)