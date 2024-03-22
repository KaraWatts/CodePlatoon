from django.core.exceptions import ValidationError
import re

def validate_name_format(value):
    """
    Validator for the "First M. Last" name format.
    """
    name_pattern = re.compile(r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$')
    if not name_pattern.match(value):
        raise ValidationError('Name must be in the format "First Middle Initial. Last"')

def validate_school_email(value):
    """
    Validator for the school email format ending with "@school.com".
    """
    email_pattern = re.compile(r'^.+@school\.com$')
    if not email_pattern.match(value):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

def validate_combination_format(value):
    """
    Validator for the format "12-12-12" (ensures there are numbers only).
    """
    combination_pattern = re.compile(r'^\d{2}-\d{2}-\d{2}$')
    if not combination_pattern.match(value):
        raise ValidationError('Combination must be in the format "12-12-12"')
