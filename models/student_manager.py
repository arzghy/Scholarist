# models/student_manager.py
# Kelas untuk manajemen data siswa

from models.json_manager import JSONManager

class StudentManager:
    def __init__(self):
        self.data_manager = JSONManager('student_data.json')
    
    def add_student(self, name, nisn, dob, kelas, enrollment_year, password):
        student_data = {
            'name': name,
            'nisn': nisn,
            'dob': dob,
            'kelas': kelas,
            'enrollment_year': enrollment_year,
            'password': password
        }
        self.data_manager.add(student_data)
        print("Data siswa berhasil ditambahkan.")
    
    def update_student(self, nisn, new_data):
        result = self.data_manager.update(nisn, 'nisn', new_data)
        if result:
            print("Data siswa berhasil diperbarui.")
        else:
            print("Siswa dengan NISN tersebut tidak ditemukan.")
    
    def delete_student(self, nisn):
        self.data_manager.delete(nisn, 'nisn')
        print("Data siswa berhasil dihapus.")
    
    def get_all_students(self):
        return self.data_manager.get_all()
    
    def get_student_by_nisn(self, nisn):
        return self.data_manager.get_by_key(nisn, 'nisn')
    
    def search_student(self, key, value):
        return self.data_manager.search(key, value)
    
    def sort_students(self, key, ascending=True):
        return self.data_manager.sort(key, ascending)