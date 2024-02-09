# Build a Contact List

## This challenge will help you to

- Understand how instance variables and methods represent the characteristics and actions of an object

## Summary

Let's create a class for creating contact lists. Each contact list should store its `contacts` as a list of dictionaries, containing name and phone number. The list should be sorted by the contacts' name. The contact list should also have a `name` that distinguishes it, e.g. "School Friends", "Extended Family", or "Work Buddies".
The contact list should have 3 instance methods:

- `add_contact({})` should add a new contact to the list, while keeping the list sorted
- `remove_contact('Alice')` should remove a contact from the list by name.
- `find_shared_contacts(ContactList)` should accept another contact list as an argument, and then return a new list of dictionaries to indicate all the contacts that appear in both lists (exact same name and phone number).

For example:

```python
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]
```

## Testing

This exercise contains a pytest test suite to help you develop your Test Driven Development skills. Use the following command to run the test suite:

```bash
 pytest test_contact_list.py
```
