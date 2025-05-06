# models/school_manager.py
# Kelas untuk manajemen data sekolah

from models.json_manager import JSONManager

class SchoolManager:
    def __init__(self):
        self.data_manager = JSONManager('school_data.json')
    
    def add_school(self, name, location, npsn):
        school_data = {
            'name': name,
            'location': location,
            'npsn': npsn
        }
        self.data_manager.add(school_data)
        print("Data sekolah berhasil ditambahkan.")
    
    def update_school(self, npsn, new_data):
        result = self.data_manager.update(npsn, 'npsn', new_data)
        if result:
            print("Data sekolah berhasil diperbarui.")
        else:
            print("Sekolah dengan NPSN tersebut tidak ditemukan.")
    
    def delete_school(self, npsn):
        self.data_manager.delete(npsn, 'npsn')
        print("Data sekolah berhasil dihapus.")
    
    def get_all_schools(self):
        return self.data_manager.get_all()
    
    def get_school_by_npsn(self, npsn):
        return self.data_manager.get_by_key(npsn, 'npsn')