# This will allow us to throw a validation error when interacting with 
# our models.
from django.core.exceptions import ValidationError
# This will allow us to search through our string to match our regex function
import re


# This will allow us to throw a validation error when interacting with 
# our models.
from django.core.exceptions import ValidationError
# This will allow us to search through our string to match our regex function
import re

def validate_name(name):
    error_message = "Improper name format"
    # Message we want to give the user when passing incorrect input
    regex = r'^[A-Z][a-z]*$'
    # ^: The caret symbol denotes the start of the string.
    # [A-Z]: This matches a single capital letter at the beginning of the string.
    # [a-z]*: This matches zero or more occurrences of any alphabetic character (both uppercase and lowercase) after the first capital letter.
    # $: The dollar sign denotes the end of the string.
    good_name = re.match(regex, name)
    # returns a boolean value [True || False]
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={ 'name' : name })
    
def validate_type(value):
    allowed_types = ['rock', "normal", 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy', 'unknown', 'shadow']
    
    if value.lower() not in allowed_types:
        raise ValidationError(f"Invalid type: {value}. Please choose from {', '.join(allowed_types)}.")
