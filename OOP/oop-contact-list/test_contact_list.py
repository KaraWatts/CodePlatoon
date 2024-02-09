from contact_list import ContactList

def test_add_contact():
    contacts = [{'name': 'Alice', 'number': '123-4567'}]
    my_list = ContactList('My List', contacts)
    my_list.add_contact({'name': 'Bob', 'number': '987-6543'})
    assert len(my_list.get_contacts) == 2
    assert my_list.get_contacts[0]['name'] == 'Alice'
    assert my_list.get_contacts[1]['name'] == 'Bob'

def test_remove_contact():
    contacts = [{'name': 'Alice', 'number': '123-4567'}, {'name': 'Bob', 'number': '987-6543'}]
    my_list = ContactList('My List', contacts)
    my_list.remove_contact('Alice')
    assert len(my_list.get_contacts) == 1
    assert my_list.get_contacts[0]['name'] == 'Bob'

def test_find_shared_contacts():
    friends = [{'name': 'Alice', 'number': '867-5309'}, {'name': 'Bob', 'number': '555-5555'}]
    work_buddies = [{'name': 'Alice', 'number': '867-5309'}, {'name': 'Carlos', 'number': '555-5555'}]
    my_friends_list = ContactList('My Friends', friends)
    my_work_buddies = ContactList('Work Buddies', work_buddies)
    shared_contacts = my_friends_list.find_shared_contacts(my_work_buddies)
    assert len(shared_contacts) == 1
    assert shared_contacts[0]['name'] == 'Alice'

def test_name_getter_and_setter():
    my_list = ContactList('My List', [])
    my_list.set_name = 'New Name'
    assert my_list.get_name == 'New Name'

def test_contacts_getter_and_setter():
    contacts = [{'name': 'Alice', 'number': '123-4567'}]
    my_list = ContactList('My List', contacts)
    new_contacts = [{'name': 'Bob', 'number': '987-6543'}]
    my_list.set_contacts = new_contacts
    assert my_list.get_contacts == new_contacts

# Add more test cases as needed
