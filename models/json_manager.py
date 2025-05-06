# models/json_manager.py
# Kelas untuk manajemen file JSON

import json
import os
from models.linked_list import LinkedList
from utils.algoritma import binary_search, quick_sort

class JSONManager:
    def __init__(self, filename):
        self.filename = filename
        self.linked_list = LinkedList()
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        self.linked_list.append(item)
            except json.JSONDecodeError:
                print(f"Error: File {self.filename} tidak valid.")
        else:
            # Buat file baru jika belum ada
            with open(self.filename, 'w') as file:
                json.dump([], file)
    
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.linked_list.to_list(), file, indent=4)
    
    def add(self, data):
        self.linked_list.append(data)
        self.save_data()
    
    def update(self, key, key_name, new_data):
        result = self.linked_list.update(key, key_name, new_data)
        if result:
            self.save_data()
        return result
    
    def delete(self, key, key_name):
        self.linked_list.remove(key, key_name)
        self.save_data()
    
    def get_all(self):
        return self.linked_list.to_list()
    
    def get_by_key(self, key, key_name):
        return self.linked_list.find(key, key_name)
    
    def search(self, key, value):
        data = self.linked_list.to_list()
        return binary_search(data, key, value)
    
    def sort(self, key, ascending=True):
        data = self.linked_list.to_list()
        return quick_sort(data, key, ascending)