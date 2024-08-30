#Assignment_1;
class Node:
    def __init__(self, Name, Disease, priority):
        self.name = Name
        self.disease = Disease
        self.priority = priority
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def createnode(self, Name, Disease, priority):
        new_node = Node(Name, Disease, priority)
        return new_node
    
    def insertbegin(self, Name, Disease, priority):
        new_node = self.createnode( Name, Disease, priority )
        if self.head is None:
            self.head = new_node
            return
        new_node.next = head
        head = new_node
    
    def insertmid(self, Name, Disease, priority):
        new_node = self.createnode( Name, Disease, priority )
    
    def append(self, Name, Disease, priority):
        new_node = self.createnode( Name, Disease, priority )
