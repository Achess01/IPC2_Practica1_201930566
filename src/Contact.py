class Contact:
    ids = 0
    def __init__(self, name, lastname, phone_number):
        self.id = Contact.ids        
        Contact.ids += 1
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
    
    
    def exists(self, phone_number_search):
        return self.phone_number == phone_number_search

    def isplace(self, new_contact):
        if new_contact.name.lower() == self.name.lower():
            if new_contact.lastname.lower() <= self.lastname.lower():
                return True
        elif new_contact.name.lower() < self.name.lower():
                return True
        return False