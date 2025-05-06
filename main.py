import json
import os
from datetime import datetime

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

# Fungsi untuk quick sort
def quick_sort(arr, key, ascending=True):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (x[key] < pivot[key] if ascending else x[key] > pivot[key])]
    middle = [x for x in arr if x[key] == pivot[key]]
    right = [x for x in arr if (x[key] > pivot[key] if ascending else x[key] < pivot[key])]
    
    return quick_sort(left, key, ascending) + middle + quick_sort(right, key, ascending)

# Fungsi untuk binary search
def binary_search(arr, key, value):
    # Pastikan array sudah diurutkan
    arr = quick_sort(arr, key)
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][key] == value:
            return arr[mid]
        elif arr[mid][key] < value:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

# Kelas untuk manajemen file JSON
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

# Kelas untuk manajemen data sekolah
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

# Kelas untuk manajemen data siswa
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

# Kelas untuk manajemen data guru
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

# Kelas untuk manajemen akun
class AccountManager:
    def __init__(self):
        self.admin_manager = JSONManager('admin_data.json')
        self.operator_manager = JSONManager('operator_data.json')
        self.student_manager = StudentManager()
        self.teacher_manager = TeacherManager()
    
    def register_admin(self, username, password):
        admin_data = {
            'username': username,
            'password': password
        }
        self.admin_manager.add(admin_data)
        print("Akun administrator berhasil dibuat.")
    
    def register_operator(self, username, password):
        operator_data = {
            'username': username,
            'password': password
        }
        self.operator_manager.add(operator_data)
        print("Akun operator sekolah berhasil dibuat.")
    
    def login_admin(self, username, password):
        admin = self.admin_manager.get_by_key(username, 'username')
        if admin and admin['password'] == password:
            return True
        return False
    
    def login_operator(self, username, password):
        operator = self.operator_manager.get_by_key(username, 'username')
        if operator and operator['password'] == password:
            return True
        return False
    
    def login_student(self, name, nisn, password):
        student = self.student_manager.get_student_by_nisn(nisn)
        if student and student['name'] == name and student['password'] == password:
            return True
        return False
    
    def login_teacher(self, nuptk, password):
        teacher = self.teacher_manager.get_teacher_by_nuptk(nuptk)
        if teacher and teacher['password'] == password:
            return True
        return False
    
    def verify_admin_identity(self, username):
        admin = self.admin_manager.get_by_key(username, 'username')
        return admin is not None
    
    def verify_operator_identity(self, username):
        operator = self.operator_manager.get_by_key(username, 'username')
        return operator is not None
    
    def verify_student_identity(self, nisn, dob):
        student = self.student_manager.get_student_by_nisn(nisn)
        return student is not None and student['dob'] == dob
    
    def verify_teacher_identity(self, nuptk, dob):
        teacher = self.teacher_manager.get_teacher_by_nuptk(nuptk)
        return teacher is not None and teacher['dob'] == dob
    
    def reset_admin_password(self, username, new_password):
        admin_data = self.admin_manager.get_all()
        for admin in admin_data:
            if admin['username'] == username:
                admin['password'] = new_password
                self.admin_manager.save_data()
                return True
        return False
    
    def reset_operator_password(self, username, new_password):
        operator_data = self.operator_manager.get_all()
        for operator in operator_data:
            if operator['username'] == username:
                operator['password'] = new_password
                self.operator_manager.save_data()
                return True
        return False
    
    def reset_student_password(self, nisn, new_password):
        student_data = self.student_manager.get_all_students()
        for student in student_data:
            if student['nisn'] == nisn:
                student['password'] = new_password
                self.student_manager.data_manager.save_data()
                return True
        return False
    
    def reset_teacher_password(self, nuptk, new_password):
        teacher_data = self.teacher_manager.get_all_teachers()
        for teacher in teacher_data:
            if teacher['nuptk'] == nuptk:
                teacher['password'] = new_password
                self.teacher_manager.data_manager.save_data()
                return True
        return False

# Kelas utama aplikasi
# main.py
# File utama untuk menjalankan aplikasi

import os
from models.account_manager import AccountManager
from route.administrator import AdministratorRoute
from route.guru import GuruRoute
from route.siswa import SiswaRoute
from route.operator_sekolah import OperatorSekolahRoute

class SchoolManagementSystem:
    def __init__(self):
        self.account_manager = AccountManager()
        self.current_user = None
        self.user_type = None
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("SISTEM MANAJEMEN SEKOLAH".center(50))
        print("=" * 50)
        print("1. Login sebagai Administrator")
        print("2. Login sebagai Guru")
        print("3. Login sebagai Siswa")
        print("4. Login sebagai Operator Sekolah")
        print("5. Register")
        print("0. Keluar")
        print("=" * 50)
    
    def display_register_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("REGISTER AKUN".center(50))
        print("=" * 50)
        print("1. Register sebagai Administrator")
        print("2. Register sebagai Guru")
        print("3. Register sebagai Siswa")
        print("4. Register sebagai Operator Sekolah")
        print("0. Kembali")
        print("=" * 50)
    
    def login_admin(self):
        self.clear_screen()
        print("=" * 50)
        print("LOGIN ADMINISTRATOR".center(50))
        print("=" * 50)
        
        username = input("Username: ")
        password = input("Password: ")
        
        if self.account_manager.login_admin(username, password):
            self.current_user = username
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            return True
        else:
            print("Login gagal. Username atau password salah.")
            print("\n1. Coba lagi")
            print("0. Kembali")
            choice = input("Pilih menu (0-1): ")
            
            if choice == '1':
                return self.login_admin()
            
            return False
    
    def login_teacher(self):
        self.clear_screen()
        print("=" * 50)
        print("LOGIN GURU".center(50))
        print("=" * 50)
        
        nuptk = input("NUPTK: ")
        password = input("Password: ")
        
        if self.account_manager.login_teacher(nuptk, password):
            self.current_user = nuptk
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            return True
        else:
            print("Login gagal. NUPTK atau password salah.")
            print("\n1. Coba lagi")
            print("2. Ajukan Reset Password")
            print("0. Kembali")
            choice = input("Pilih menu (0-2): ")
            
            if choice == '1':
                return self.login_teacher()
            elif choice == '2':
                self.request_reset_password('guru', nuptk)
            
            return False
    
    def login_student(self):
        self.clear_screen()
        print("=" * 50)
        print("LOGIN SISWA".center(50))
        print("=" * 50)
        
        name = input("Nama: ")
        nisn = int(input("NISN: "))
        password = input("Password: ")
        
        if self.account_manager.login_student(name, nisn, password):
            self.current_user = {
                "name": name,
                "nisn": nisn,
                "password": password
            }
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            return True
        else:
            print("Login gagal. Nama atau NISN atau password salah.")
            print("\n1. Coba lagi")
            print("2. Ajukan Reset Password")
            print("0. Kembali")
            choice = input("Pilih menu (0-2): ")
            
            if choice == '1':
                return self.login_student()
            elif choice == '2':
                self.request_reset_password('siswa', nisn)
            
            return False
    
    def login_operator(self):
        self.clear_screen()
        print("=" * 50)
        print("LOGIN OPERATOR SEKOLAH".center(50))
        print("=" * 50)
        
        username = input("Username: ")
        password = input("Password: ")
        
        if self.account_manager.login_operator(username, password):
            self.current_user = username
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            return True
        else:
            print("Login gagal. Username atau password salah.")
            print("\n1. Coba lagi")
            print("2. Ajukan Reset Password")
            print("0. Kembali")
            choice = input("Pilih menu (0-2): ")
            
            if choice == '1':
                return self.login_operator()
            elif choice == '2':
                self.request_reset_password('operator', username)
            
            return False
    
    def request_reset_password(self, user_type, user_id):
        """
        Mengajukan permintaan reset password ke administrator
        
        Args:
            user_type (str): Jenis pengguna ('guru', 'siswa', 'operator')
            user_id (str): ID pengguna (NUPTK, NISN, atau username)
        """
        self.clear_screen()
        print("=" * 50)
        print("AJUKAN PERMINTAAN RESET PASSWORD".center(50))
        print("=" * 50)
        
        # Cek apakah pengguna sudah memiliki permintaan yang masih pending
        existing_request = self.account_manager.get_user_pending_reset_request(user_type, user_id)
        if existing_request:
            print("Anda sudah memiliki permintaan reset password yang masih pending.")
            print(f"Permintaan diajukan pada: {existing_request['request_date']}")
            print(f"Status: {existing_request['status']}")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        # Verifikasi identitas pengguna
        if user_type == 'guru':
            dob = input("Tanggal Lahir (DD-MM-YYYY): ")
            if not self.account_manager.verify_teacher_identity(user_id, dob):
                print("NUPTK atau tanggal lahir tidak valid.")
                input("Tekan Enter untuk melanjutkan...")
                return
        elif user_type == 'siswa':
            dob = input("Tanggal Lahir (DD-MM-YYYY): ")
            if not self.account_manager.verify_student_identity(user_id, dob):
                print("NISN atau tanggal lahir tidak valid.")
                input("Tekan Enter untuk melanjutkan...")
                return
        elif user_type == 'operator':
            if not self.account_manager.verify_operator_identity(user_id):
                print("Username tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                return
        
        # Ajukan permintaan reset password
        new_pass = input("Masukkan password baru: ")
        if self.account_manager.request_reset_password(user_type, user_id, new_pass):
            print("Permintaan reset password berhasil diajukan.")
            print("Administrator akan memproses permintaan Anda.")
        else:
            print("Gagal mengajukan permintaan reset password.")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def register(self):
        self.display_register_menu()
        choice = input("Pilih jenis akun (0-4): ")
        
        if choice == '1':  # Administrator
            self.clear_screen()
            print("Register sebagai Administrator")
            username = input("Username: ")
            password = input("Password: ")
            self.account_manager.register_admin(username, password)
        elif choice == '2':  # Guru
            self.clear_screen()
            print("Register sebagai Guru")
            name = input("Nama: ")
            nuptk = int(input("NUPTK: "))
            dob = int(input("Tahun Lahir (YYYY): "))
            subjects = input("Mata Pelajaran (pisahkan dengan koma): ").split(',')
            password = input("Password: ")
            self.account_manager.teacher_manager.add_teacher(name, nuptk, dob, subjects, password)
        elif choice == '3':  # Siswa
            self.clear_screen()
            print("Register sebagai Siswa")
            name = input("Nama: ")
            nisn = input("NISN: ")
            dob = int(input("Tahun Lahir (YYYY): "))
            kelas = input("Kelas: ")
            enrollment_year = input("Tahun Masuk: ")
            password = input("Password: ")
            self.account_manager.student_manager.add_student(name, nisn, dob, kelas, enrollment_year, password)
        elif choice == '4':  # Operator Sekolah
            self.clear_screen()
            print("Register sebagai Operator Sekolah")
            username = input("Username: ")
            password = input("Password: ")
            self.account_manager.register_operator(username, password)
        elif choice == '0':
            return
        else:
            print("Pilihan tidak valid.")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Pilih menu (0-5): ")
            
            if choice == '1':  # Login sebagai Administrator
                if self.login_admin():
                    admin_route = AdministratorRoute(self.current_user, self.account_manager)
                    admin_route.run()
                    self.current_user = None
            elif choice == '2':  # Login sebagai Guru
                if self.login_teacher():
                    guru_route = GuruRoute(self.current_user)
                    guru_route.run()
                    self.current_user = None
            elif choice == '3':  # Login sebagai Siswa
                if self.login_student():
                    siswa_route = SiswaRoute(self.current_user)
                    siswa_route.run()
                    self.current_user = None
            elif choice == '4':  # Login sebagai Operator Sekolah
                if self.login_operator():
                    operator_route = OperatorSekolahRoute(self.current_user)
                    operator_route.run()
                    self.current_user = None
            elif choice == '5':  # Register
                self.register()
            elif choice == '0':  # Keluar
                print("Terima kasih telah menggunakan Sistem Manajemen Sekolah.")
                break
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan...")

# Menjalankan aplikasi
if __name__ == "__main__":
    # Buat folder models dan route jika belum ada
    if not os.path.exists('models'):
        os.makedirs('models')
    if not os.path.exists('route'):
        os.makedirs('route')
    
    app = SchoolManagementSystem()
    app.run()