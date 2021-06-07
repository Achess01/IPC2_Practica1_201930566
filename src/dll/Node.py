from src.Contact import Contact

from .. import Contact
class Node:
    
    def __init__(self, contact: Contact):
        self.contact = contact
    
    def set_next(self, next_contact: Contact):
        self.next = next_contact
    
    def set_prev(self, prev_contact: Contact):
        self.prev = prev_contact