from .Node import Node
from ..Contact import Contact

class List:
    def __init__(self):
        self.head = None
      
    def add(self, name, lastname, phone_number):        
        contact = Contact(name, lastname, phone_number)
        node = Node(contact)
        if self.head == None:
            self.head = node
            self.head.set_next(None)
            self.head.set_prev(None)
        else:
            aux = self.head                         
            while aux != None:
                if aux.contact.isplace(contact):                    
                    node.set_next(aux)
                    node.set_prev(aux.get_prev)         
                    aux.set_prev(node)                               
                    break                
                if(aux.get_next() == None):
                    aux.set_next(node)
                    node.set_prev(aux)
                    node.set_next(None)
                aux = aux.get_next()
                               
    # Retorna None si el usuario no existe.
    def search(self, phone_number):
        if self.head != None:
            aux = self.head
            while(aux != None):
                if aux.contact.exists(phone_number):
                    return aux.contact
                aux = aux.get_next()        
        return None
    
    def show(self):
        aux = self.head
        while(aux != None):
            print(aux.contact.name)
            print(aux.contact.lastname)
            print(aux.contact.phone_number)
            print("=====")
            aux = aux.get_next()