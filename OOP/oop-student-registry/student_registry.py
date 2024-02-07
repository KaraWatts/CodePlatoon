import re

class Student:
    """Student class for use in school registry"""
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = 'Invalid'
        self._age = 'Invalid'
        self._grade = 'Invalid'

        self.set_name = name
        self.set_age = age
        self.set_grade = grade

    def __str__(self) :
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"

    # Helper methods
    def convert_grade(self, grade) :
        return int(grade[:-2])

    # Getters and Setters
    @property
    def get_name(self) :
        """Gets the name property

        Args:
            none
        Returns:
            Student name
        """
        return self._name
    
    @get_name.setter
    def set_name(self, name) : 
        """Updates students name only if the name is 3 or more characters, holds no spaces or special characters and is in title format
        
        Args:
            name Name to set
        Returns:
            Message only on fail
        """
        re_pattern = r"^[a-zA-Z]{3,}$"
        matches = re.match(re_pattern, f"{name}")
        if matches == None:
             print("Enter a valid name: 3 characters or more")
        else:
            self._name = name.title()

    @property
    def get_age(self) :
        """Gets the student age

        Args:
            none
        Returns:
            Student age
        """
        return self._age

    @get_age.setter
    def set_age(self, age) :
        """Sets student age if greater than 11 or less than 18

        Args:
            age Age as an integer
        Returns:
            Message only on fail
        """
        if type(age) == int and 11 < age < 18 :
            self._age = age
        else: print("Invalid age: outside of age range (12-17)")
        

    @property
    def get_grade(self) :
        """Gets student grade

        Args:
            None
        Returns:
            Student grade as string
        """
        return self._grade

    @get_grade.setter
    def set_grade(self, grade) :
        """Sets student grade if within 9-12th as a string

        Args:
            grade Student grade as string - including 'th'
        Returns:
            Message on fail
        """
        re_pattern = r'^1?\dth$'
        matches = re.match(re_pattern, f'{grade}')
        if matches == None:
             print("Enter a valid grade as string")
        elif  8 < self.convert_grade(grade) < 13:
            self._grade = grade
            # return True
        else: print("Outside of grade range (9-12 only)")

    # Methods
    def advance(self, years = 1) :
        """Adds years to current grade if valid

        Args:
            years Number of years to add
        Returns:
            Success or Fail message
        """
        grade = self.convert_grade(self.get_grade)
        # Assign graduation status after 12th grade
        if grade + 1 > 12:
            self._grade = 'Graduated'
            return f"{self.get_name} has Graduated 🎉"
        # Ensure advance statement only cannot be decremented with negative values
        elif grade + 1 < grade:
            return 'Cannot go back a grade'
        
        grade += years
        grade = f"{grade}th"

        # Calls grade into grade setting and captures any invalid entry output into grade_result
        self.set_grade = grade

        return f"{self.get_name} has advanced to the {self.get_grade} grade"


    def study(self, subject) -> str:
        """"Displays message describing subject studying

        Args:
            subject Subject studying
        Returns:
            Message including subject
        """
        return f"{self.get_name} is studying {str(subject).title()}"