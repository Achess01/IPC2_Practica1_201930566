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