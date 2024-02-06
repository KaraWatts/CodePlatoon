# CSV Reader

In this exercise, you will create a python program for a pet adoption center that can read data about various adoptable animals from CSV files, based on user input. In the included sample data, there are already two CSV files, containing information about cats and dogs. 


## Challenge

Write a program that lets a user input a type of animal at the command line, and then displays information about those animals from the appropriate CSV file. You'll need to use python's [open method](https://docs.python.org/3/library/functions.html#open) to read the file, and then the [CSV module](https://docs.python.org/3/library/csv.html) to parse the data into a python data structure, like a list or dictionary. The output for an individual animal should be formatted like an english sentence, like "fido is a 4 year old husky."
- Use try/except to handle bad input. Python will throw an error if we try to read a file that doesn't exist, but we want to give a meaningful response to the user in all cases. For example, your program will fail to open a CSV file if the user specifies "birds", because we only have data for "cats" and "dogs". In this case, the output to the user should be "Sorry, we don't have any birds here". 
- Right before the program finishes, make sure to close the file that was opened. 
- STRETCH: Refactor your solution to use python's [with statement](https://www.geeksforgeeks.org/with-statement-in-python/). This is an advanced python feature that helps you automatically perform certain mundane actions, like closing files after you're done reading them. 

## Resources 
[Reading and writing csvs in python](https://realpython.com/python-csv/)
