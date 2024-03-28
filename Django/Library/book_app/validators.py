from django.core.exceptions import ValidationError
import re

def validate_title_case(name):
    if name != name.title():
        raise ValidationError('Input must be in title format')
    else:
        return name
    
def validate_isbn(isbn):
    regex = r'^[0-9]{3}\-[0-9]{10}$'

    if re.match(regex, isbn):
        return isbn
    else:
        raise ValidationError('Must be a valid ISBN ex. 123-1234567890')