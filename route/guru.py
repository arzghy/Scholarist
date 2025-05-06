# route/guru.py
# Implementasi menu dan fungsi untuk guru

import os
from models.teacher_manager import TeacherManager
from models.student_manager import StudentManager

class GuruRoute:
    def __init__(self, current_user):
        self.current_user = current_user
        self.teacher_manager = TeacherManager()
        self.student_manager = StudentManager()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("MENU GURU".center(50))
        print("=" * 50)
        print("1. Lihat Data Pribadi")
        print("2. Update Data Pribadi")
        print("3. Lihat Data Siswa")
        print("0. Logout")
        print("=" * 50)
    
    def view_teacher_data(self):
        self.clear_screen()
        print("Data Pribadi Guru")
        teacher = self.teacher_manager.get_teacher_by_nuptk(self.current_user)
        if teacher:
            print(f"Nama: {teacher['name']}")
            print(f"NUPTK: {teacher['nuptk']}")
            print(f"Tanggal Lahir: {teacher['dob']}")
            print(f"Mata Pelajaran: {', '.join(teacher['subjects'])}")
        else:
            print("Data tidak ditemukan.")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def update_teacher_data(self):
        self.clear_screen()
        print("Update Data Pribadi Guru")
        teacher = self.teacher_manager.get_teacher_by_nuptk(self.current_user)
        if not teacher:
            print("Data tidak ditemukan.")
        else:
            print(f"Data guru saat ini:")
            print(f"Nama: {teacher['name']}")
            print(f"NUPTK: {teacher['nuptk']}")
            print(f"Tanggal Lahir: {teacher['dob']}")
            print(f"Mata Pelajaran: {', '.join(teacher['subjects'])}")
            print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
            name = input("Nama: ") or teacher['name']
            dob = input("Tanggal Lahir (DD-MM-YYYY): ") or teacher['dob']
            subjects_input = input("Mata Pelajaran (pisahkan dengan koma): ")
            subjects = subjects_input.split(',') if subjects_input else teacher['subjects']
            password = input("Password (kosongkan jika tidak ingin mengubah): ")
            
            new_data = {
                'name': name,
                'nuptk': self.current_user,
                'dob': dob,
                'subjects': subjects,
                'password': password if password else teacher['password']
            }
            self.teacher_manager.update_teacher(self.current_user, new_data)
        
        input("Tekan Enter untuk melanjutkan...")
    
    def view_student_data(self):
        self.clear_screen()
        print("Data Siswa")
        students = self.student_manager.get_all_students()
        if not students:
            print("Tidak ada data siswa.")
        else:
            for i, student in enumerate(students, 1):
                print(f"{i}. Nama: {student['name']}")
                print(f"   NISN: {student['nisn']}")
                print(f"   Kelas: {student['kelas']}")
                print("-" * 30)
        input("Tekan Enter untuk melanjutkan...")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Pilih menu (0-3): ")
            
            if choice == '1':  # Lihat Data Pribadi
                self.view_teacher_data()
            elif choice == '2':  # Update Data Pribadi
                self.update_teacher_data()
            elif choice == '3':  # Lihat Data Siswa
                self.view_student_data()
            elif choice == '0':  # Logout
                break
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan...")
        
        return None  # Mengembalikan None untuk menandakan logout