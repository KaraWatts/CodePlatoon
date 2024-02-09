
class ContactList:
    def __init__(self, list_name, contact_list = []):
        self.contact_list = contact_list
        self.list_name = list_name
    
    def add_contact(self, new_list):
        self.contact_list.append(new_list)

    def remove_contact(self, cont_name):
        for contact in self.contact_list:
            if cont_name == contact['name']:
                self.contact_list.remove(contact)

    def find_shared_contacts(self, new_cont_list):
        shared_contacts = []
        for contact in new_cont_list.get_contacts:
            if contact in self.contact_list:
                shared_contacts.append(contact)
        return shared_contacts

        
    @property 
    def get_contacts(self):
        return self.contact_list
    
    @get_contacts.setter
    def set_contacts(self,person_to_add):
        self.contact_list = person_to_add

    @property 
    def get_name(self):
        return self.list_name
    
    @get_name.setter
    def set_name(self,new_list_name):
        self.list_name = new_list_name

# contacts = [{'name': 'Alice', 'number': '123-4567'}, {'name': 'Bob', 'number': '987-6543'}]
# my_list = ContactList('My List', contacts)
# my_list.remove_contact('Alice')
# print(my_list.get_contacts)
        
        