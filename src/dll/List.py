from .Node import Node
from ..Contact import Contact
from graphviz import Digraph

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
                if aux.contact.is_place(contact):                            
                    aux2 = aux.get_prev()                    
                    node.set_prev(aux2)
                    if aux2 != None:
                        aux2.set_next(node)
                    node.set_next(aux)
                    aux.set_prev(node)
                    if aux == self.head:
                        self.head = node
                    break
                if aux.get_next() == None:
                    aux.set_next(node)
                    node.set_prev(aux)
                    node.set_next(None)
                    break
                aux = aux.get_next()             
               
                
                               
    # Retorna None si el usuario no existe.
    def search(self, phone_number):
        if self.head != None:
            aux = self.head
            while aux != None:
                if aux.contact.exists(phone_number):
                    return aux.contact
                aux = aux.get_next()        
        return None
    
    def show(self):
        dot = Digraph(format='png', filename='agenda.gv',
        node_attr={'color': 'lightblue2', 'style': 'filled'})     
        dot.attr(label='\nAGENDA')
        dot.attr('node', shape='box')        
        aux = self.head
        while aux != None:   
            contact_aux = aux.contact
            text = 'Nombre: ' + contact_aux.name + '\nApellido: ' + contact_aux.lastname + '\nTeléfono: ' + str(contact_aux.phone_number)
            dot.node('node' + str(contact_aux.id), text)                     
            aux = aux.get_next()
        aux = self.head
        while aux != None:                  
            if aux.get_next() != None:                
                
                dot.edge('node' + str(aux.contact.id), 'node' + str(aux.get_next().contact.id), dir="both")         
            aux = aux.get_next()
        dot.view()