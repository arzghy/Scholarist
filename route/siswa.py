# route/siswa.py
# Implementasi menu dan fungsi untuk siswa

import os
from models.student_manager import StudentManager

class SiswaRoute:
    def __init__(self, current_user):
        self.current_user = current_user
        self.student_manager = StudentManager()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("MENU SISWA".center(50))
        print("=" * 50)
        print("1. Lihat Data Pribadi")
        print("2. Update Data Pribadi")
        print("0. Logout")
        print("=" * 50)
    
    def view_student_data(self):
        self.clear_screen()
        print("Data Pribadi Siswa")
        student = self.student_manager.get_student_by_nisn(self.current_user)
        if student:
            print(f"Nama: {student['name']}")
            print(f"NISN: {student['nisn']}")
            print(f"Tahun Lahir: {student['dob']}")
            print(f"Kelas: {student['kelas']}")
            print(f"Tahun Masuk: {student['enrollment_year']}")
        else:
            print("Data tidak ditemukan.")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def update_student_data(self):
        self.clear_screen()
        print("Update Data Pribadi Siswa")
        student = self.student_manager.get_student_by_nisn(self.current_user)
        if not student:
            print("Data tidak ditemukan.")
        else:
            print(f"Data siswa saat ini:")
            print(f"Nama: {student['name']}")
            print(f"NISN: {student['nisn']}")
            print(f"Tanggal Lahir: {student['dob']}")
            print(f"Kelas: {student['kelas']}")
            print(f"Tahun Masuk: {student['enrollment_year']}")
            print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
            name = input("Nama: ") or student['name']
            dob = input("Tanggal Lahir (DD-MM-YYYY): ") or student['dob']
            password = input("Password (kosongkan jika tidak ingin mengubah): ")
            
            new_data = {
                'name': name,
                'nisn': self.current_user,
                'dob': dob,
                'kelas': student['kelas'],
                'enrollment_year': student['enrollment_year'],
                'password': password if password else student['password']
            }
            self.student_manager.update_student(self.current_user, new_data)
        
        input("Tekan Enter untuk melanjutkan...")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Pilih menu (0-2): ")
            
            if choice == '1':  # Lihat Data Pribadi
                self.view_student_data()
            elif choice == '2':  # Update Data Pribadi
                self.update_student_data()
            elif choice == '0':  # Logout
                break
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan...")
        
        return None  # Mengembalikan None untuk menandakan logout   