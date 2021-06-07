from src.Contact import Contact
class Node:
    
    def __init__(self, contact: Contact):
        self.contact = contact
        self.next = None
        self.prev = None
    
    def set_next(self, next_node):
        self.next = next_node
    
    def get_next(self):
        return self.next
    
    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_prev(self):
        return self.prev        