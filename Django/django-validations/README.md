# Validations

More than just preventing "bad" or "incomplete" data, an application's models can enforce domain rules & requirements. Most applications take a layered approach to data integrity.

| Database | Model        | Interface   |
|----------|--------------|-------------|
| Core     | Middle Layer | Outer Layer |


### Interface
At the outermost layer, you have the program's interface, e.g. an HTML form that only allows a user to enter an email address that contains `@`.

### Model
The next level of validation is often performed by the application's models. One approach might be to overwrite the `.save` method like so:

```Python
def save(self, *args, **kwargs):
    if len(self.first_name) < 1
        raise ValidationError(_('Name must be longer than one letter'), code='invalid')

    super(SwimRecord, self).save(*args, **kwargs)
   
```

While this works, it isn't very scalable. [Django](https://docs.djangoproject.com/en/3.0/ref/validators/) takes a different approach. 

### Database
The final level of validation is usually performed by the database. Often with `NOT NULL` constraints or particular column types (`integer` vs `varchar(255)` or `char(14)`).

-----
## Challenge
You are maintaining a database for an application that lets users upload record-breaking swim records, including the swimmer's name, their team's name, the type of race, and when they broke the record. Unfortunately, many users are submitting records with missing or incorrect data:
- Some records are missing the swimmers name, or their team's name
- Some records are submitted for unofficial races (the race is too short, or an illegal swim stroke was used)
- Some records have impossible dates (the record was broken in the future, or before the original records was set)
Use Django validators to ensure that bad data cannot be inserted into the database, and that a meaningful error message is generated that briefly describes why the data could not be inserted into the database. Read the tests in `tests.py` to see the exact requirements.


This challenge will have you exploring the Django docs (and any other resources you find online) to resolve some errors and ultimately make the tests pass. We are working with one model. The attributes are written for you and commented out - they are also incomplete. You'll have to add some settings to what is there to get the first few tests to pass.

The last batch of tests will require you to write your own validations. 

### Release 0: Setup
Create a virtual env. Start it up. Then tell pip to read the `requirements.txt` file and install all the requirements. 

```
python -m venv venv 

source venv/bin/activate

pip install -r requirements.txt
```

### Release 1
Run the test with the following command. 
```bash
python manage.py test
```

The first four tests will pass because of the nature of `full_clean()`. We've commented out the attributes in the model. Your job is to figure out what code needs to be added to each attribute to truly pass each test.

If you get an error saying the test db already exists you should be able to type `yes` to destroy it and create a new one.

Using the skeleton found in `models.py`, your job is to uncomment out each column one by one and make the tests pass.

### Release 2
This challenge includes one model `SwimRecord`. Follow the tests in `swimrecords/tests.py`, adding any missing validations using those provided by [Django](https://docs.djangoproject.com/en/2.1/ref/validators/)

Some validations can be implemented by using functions provided by Django, but for some tests, you'll need to create your own validation methods.
