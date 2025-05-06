# models/teacher_manager.py
# Kelas untuk manajemen data guru

from models.json_manager import JSONManager

class TeacherManager:
    def __init__(self):
        self.data_manager = JSONManager('teacher_data.json')
    
    def add_teacher(self, name, nuptk, dob, subjects, password):
        teacher_data = {
            'name': name,
            'nuptk': nuptk,
            'dob': dob,
            'subjects': subjects,
            'password': password
        }
        self.data_manager.add(teacher_data)
        print("Data guru berhasil ditambahkan.")
    
    def update_teacher(self, nuptk, new_data):
        result = self.data_manager.update(nuptk, 'nuptk', new_data)
        if result:
            print("Data guru berhasil diperbarui.")
        else:
            print("Guru dengan NUPTK tersebut tidak ditemukan.")
    
    def delete_teacher(self, nuptk):
        self.data_manager.delete(nuptk, 'nuptk')
        print("Data guru berhasil dihapus.")
    
    def get_all_teachers(self):
        return self.data_manager.get_all()
    
    def get_teacher_by_nuptk(self, nuptk):
        return self.data_manager.get_by_key(nuptk, 'nuptk')
    
    def search_teacher(self, key, value):
        return self.data_manager.search(key, value)
    
    def sort_teachers(self, key, ascending=True):
        return self.data_manager.sort(key, ascending)