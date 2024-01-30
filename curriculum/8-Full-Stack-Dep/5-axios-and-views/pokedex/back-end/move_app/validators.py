from django.core.exceptions import ValidationError
import re

def validate_move_name(name):
    regex = r"^[a-zA-Z]+ ?[a-zA-Z]+$"
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError("Improper Format")