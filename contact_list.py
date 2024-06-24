class ContactList:

    def __init__(self, group_name, contacts):
        self.group_name = group_name
        self.contacts = contacts

    def __repr__(self):
        return f"{self.group_name} -- {self.contacts}"
    
    def add_contact(self, contact_info):
        for contact in self.contacts:
            if (contact['name']).lower() == (contact_info['name']).lower():
                    return f"Your contact {(contact_info['name']).title()} already exists in your directory!"
            else:
                self.contacts.append(contact_info)
                self.contacts = sorted(self.contacts, key=lambda x: (x['name']))
                return self.contacts
            
    def remove_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if (contact['name']).lower() == name.lower():
                self.contacts.pop(i)
                return f"Contact {contact['name']} has succesfully been removed"
        print("Contact does not exist!")
    
    def find_shared_contacts(self, contact_list):
        shared_contacts = []
        
        for contact_one in contact_list.contacts:
            for contact_two in self.contacts:
                if (contact_one['name']).lower() == (contact_two['name']).lower():
                    shared_contacts.append(contact_one)
        return shared_contacts