# models/linked_list.py
# Implementasi Linked List untuk menyimpan data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def remove(self, key, key_name):
        if not self.head:
            return
        
        if self.head.data[key_name] == key:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.data[key_name] != key:
            current = current.next
        
        if current.next:
            current.next = current.next.next
    
    def update(self, key, key_name, new_data):
        current = self.head
        while current and current.data[key_name] != key:
            current = current.next
        
        if current:
            current.data.update(new_data)
            return True
        return False
    
    def find(self, key, key_name):
        current = self.head
        while current and current.data[key_name] != key:
            current = current.next
        
        return current.data if current else None
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result