# route/administrator.py
# Implementasi menu dan fungsi untuk administrator

import os
from models.school_manager import SchoolManager
from models.student_manager import StudentManager
from models.teacher_manager import TeacherManager

class AdministratorRoute:
    def __init__(self, current_user, account_manager):
        self.current_user = current_user
        self.account_manager = account_manager
        self.school_manager = SchoolManager()
        self.student_manager = StudentManager()
        self.teacher_manager = TeacherManager()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("MENU ADMINISTRATOR".center(50))
        print("=" * 50)
        print("1. Manajemen Data Sekolah")
        print("2. Manajemen Data Siswa")
        print("3. Manajemen Data Guru")
        print("4. Kelola Permintaan Reset Password")
        print("0. Logout")
        print("=" * 50)
    
    def display_school_management_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("MANAJEMEN DATA SEKOLAH".center(50))
        print("=" * 50)
        print("1. Tambah Data Sekolah")
        print("2. Lihat Semua Data Sekolah")
        print("3. Update Data Sekolah")
        print("4. Hapus Data Sekolah")
        print("0. Kembali")
        print("=" * 50)
    
    def display_student_management_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("MANAJEMEN DATA SISWA".center(50))
        print("=" * 50)
        print("1. Tambah Data Siswa")
        print("2. Lihat Semua Data Siswa")
        print("3. Cari Data Siswa")
        print("4. Update Data Siswa")
        print("5. Hapus Data Siswa")
        print("6. Urutkan Data Siswa")
        print("0. Kembali")
        print("=" * 50)
    
    def display_teacher_management_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("MANAJEMEN DATA GURU".center(50))
        print("=" * 50)
        print("1. Tambah Data Guru")
        print("2. Lihat Semua Data Guru")
        print("3. Cari Data Guru")
        print("4. Update Data Guru")
        print("5. Hapus Data Guru")
        print("6. Urutkan Data Guru")
        print("0. Kembali")
        print("=" * 50)
    
    def display_reset_password_menu(self):
        self.clear_screen()
        print("=" * 50)
        print("KELOLA PERMINTAAN RESET PASSWORD".center(50))
        print("=" * 50)
        print("1. Lihat Permintaan Pending")
        print("2. Lihat Semua Permintaan")
        print("3. Proses Permintaan")
        print("0. Kembali")
        print("=" * 50)
    
    def manage_school_data(self):
        while True:
            self.display_school_management_menu()
            choice = input("Pilih menu (0-4): ")
            
            if choice == '1':  # Tambah Data Sekolah
                self.clear_screen()
                print("Tambah Data Sekolah")
                name = input("Nama Sekolah: ")
                location = input("Lokasi: ")
                npsn = input("NPSN: ")
                self.school_manager.add_school(name, location, npsn)
            elif choice == '2':  # Lihat Semua Data Sekolah
                self.clear_screen()
                print("Data Sekolah")
                schools = self.school_manager.get_all_schools()
                if not schools:
                    print("Tidak ada data sekolah.")
                else:
                    for i, school in enumerate(schools, 1):
                        print(f"{i}. Nama: {school['name']}")
                        print(f"   Lokasi: {school['location']}")
                        print(f"   NPSN: {school['npsn']}")
                        print("-" * 30)
            elif choice == '3':  # Update Data Sekolah
                self.clear_screen()
                print("Update Data Sekolah")
                npsn = input("NPSN Sekolah yang akan diupdate: ")
                school = self.school_manager.get_school_by_npsn(npsn)
                if not school:
                    print("Sekolah dengan NPSN tersebut tidak ditemukan.")
                else:
                    print(f"Data sekolah saat ini:")
                    print(f"Nama: {school['name']}")
                    print(f"Lokasi: {school['location']}")
                    print(f"NPSN: {school['npsn']}")
                    print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
                    name = input("Nama Sekolah: ") or school['name']
                    location = input("Lokasi: ") or school['location']
                    new_data = {
                        'name': name,
                        'location': location,
                        'npsn': npsn
                    }
                    self.school_manager.update_school(npsn, new_data)
            elif choice == '4':  # Hapus Data Sekolah
                self.clear_screen()
                print("Hapus Data Sekolah")
                npsn = input("NPSN Sekolah yang akan dihapus: ")
                confirm = input(f"Anda yakin ingin menghapus sekolah dengan NPSN {npsn}? (y/n): ")
                if confirm.lower() == 'y':
                    self.school_manager.delete_school(npsn)
            elif choice == '0':  # Kembali
                break
            else:
                print("Pilihan tidak valid.")
            
            input("Tekan Enter untuk melanjutkan...")
    
    def manage_student_data(self):
        while True:
            self.display_student_management_menu()
            choice = input("Pilih menu (0-6): ")
            
            if choice == '1':  # Tambah Data Siswa
                self.clear_screen()
                print("Tambah Data Siswa")
                name = input("Nama: ")
                nisn = input("NISN: ")
                dob = input("Tanggal Lahir (DD-MM-YYYY): ")
                kelas = input("Kelas: ")
                enrollment_year = input("Tahun Masuk: ")
                password = input("Password: ")
                self.student_manager.add_student(name, nisn, dob, kelas, enrollment_year, password)
            elif choice == '2':  # Lihat Semua Data Siswa
                self.clear_screen()
                print("Data Siswa")
                students = self.student_manager.get_all_students()
                if not students:
                    print("Tidak ada data siswa.")
                else:
                    for i, student in enumerate(students, 1):
                        print(f"{i}. Nama: {student['name']}")
                        print(f"   NISN: {student['nisn']}")
                        print(f"   Tanggal Lahir: {student['dob']}")
                        print(f"   Kelas: {student['kelas']}")
                        print(f"   Tahun Masuk: {student['enrollment_year']}")
                        print("-" * 30)
            elif choice == '3':  # Cari Data Siswa
                self.clear_screen()
                print("Cari Data Siswa")
                print("1. Cari berdasarkan Nama")
                print("2. Cari berdasarkan NISN")
                print("3. Cari berdasarkan Tanggal Lahir")
                print("4. Cari berdasarkan Kelas")
                print("5. Cari berdasarkan Tahun Masuk")
                search_choice = input("Pilih kriteria pencarian (1-5): ")
                
                if search_choice == '1':
                    key = 'name'
                    value = input("Masukkan Nama: ")
                elif search_choice == '2':
                    key = 'nisn'
                    value = input("Masukkan NISN: ")
                elif search_choice == '3':
                    key = 'dob'
                    value = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
                elif search_choice == '4':
                    key = 'kelas'
                    value = input("Masukkan Kelas: ")
                elif search_choice == '5':
                    key = 'enrollment_year'
                    value = input("Masukkan Tahun Masuk: ")
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                result = self.student_manager.search_student(key, value)
                if result:
                    print("\nHasil Pencarian:")
                    print(f"Nama: {result['name']}")
                    print(f"NISN: {result['nisn']}")
                    print(f"Tanggal Lahir: {result['dob']}")
                    print(f"Kelas: {result['kelas']}")
                    print(f"Tahun Masuk: {result['enrollment_year']}")
                else:
                    print("Data tidak ditemukan.")
            elif choice == '4':  # Update Data Siswa
                self.clear_screen()
                print("Update Data Siswa")
                nisn = input("NISN Siswa yang akan diupdate: ")
                student = self.student_manager.get_student_by_nisn(nisn)
                if not student:
                    print("Siswa dengan NISN tersebut tidak ditemukan.")
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
                    kelas = input("Kelas: ") or student['kelas']
                    enrollment_year = input("Tahun Masuk: ") or student['enrollment_year']
                    password = input("Password (kosongkan jika tidak ingin mengubah): ")
                    
                    new_data = {
                        'name': name,
                        'nisn': nisn,
                        'dob': dob,
                        'kelas': kelas,
                        'enrollment_year': enrollment_year,
                        'password': password if password else student['password']
                    }
                    self.student_manager.update_student(nisn, new_data)
            elif choice == '5':  # Hapus Data Siswa
                self.clear_screen()
                print("Hapus Data Siswa")
                nisn = input("NISN Siswa yang akan dihapus: ")
                confirm = input(f"Anda yakin ingin menghapus siswa dengan NISN {nisn}? (y/n): ")
                if confirm.lower() == 'y':
                    self.student_manager.delete_student(nisn)
            elif choice == '6':  # Urutkan Data Siswa
                self.clear_screen()
                print("Urutkan Data Siswa")
                print("1. Urutkan berdasarkan Nama")
                print("2. Urutkan berdasarkan NISN")
                print("3. Urutkan berdasarkan Tanggal Lahir")
                print("4. Urutkan berdasarkan Kelas")
                print("5. Urutkan berdasarkan Tahun Masuk")
                print("6. Kembali")
                sort_choice = input("Pilih kriteria pengurutan (1-6): ")
                
                if sort_choice == '1':
                    key = 'name'
                elif sort_choice == '2':
                    key = 'nisn'
                elif sort_choice == '3':
                    key = 'dob'
                elif sort_choice == '4':
                    key = 'kelas'
                elif sort_choice == '5':
                    key = 'enrollment_year'
                elif sort_choice == '6':
                    continue
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                order_choice = input("Urutkan secara (1) Ascending atau (2) Descending? (1/2): ")
                ascending = True if order_choice == '1' else False
                
                sorted_students = self.student_manager.sort_students(key, ascending)
                
                print("\nHasil Pengurutan:")
                for i, student in enumerate(sorted_students, 1):
                    print(f"{i}. Nama: {student['name']}")
                    print(f"   NISN: {student['nisn']}")
                    print(f"   Tanggal Lahir: {student['dob']}")
                    print(f"   Kelas: {student['kelas']}")
                    print(f"   Tahun Masuk: {student['enrollment_year']}")
                    print("-" * 30)
            elif choice == '0':  # Kembali
                break
            else:
                print("Pilihan tidak valid.")
            
            input("Tekan Enter untuk melanjutkan...")
    
    def manage_teacher_data(self):
        while True:
            self.display_teacher_management_menu()
            choice = input("Pilih menu (0-6): ")
            
            if choice == '1':  # Tambah Data Guru
                self.clear_screen()
                print("Tambah Data Guru")
                name = input("Nama: ")
                nuptk = input("NUPTK: ")
                dob = input("Tanggal Lahir (DD-MM-YYYY): ")
                subjects = input("Mata Pelajaran (pisahkan dengan koma): ").split(',')
                password = input("Password: ")
                self.teacher_manager.add_teacher(name, nuptk, dob, subjects, password)
            elif choice == '2':  # Lihat Semua Data Guru
                self.clear_screen()
                print("Data Guru")
                teachers = self.teacher_manager.get_all_teachers()
                if not teachers:
                    print("Tidak ada data guru.")
                else:
                    for i, teacher in enumerate(teachers, 1):
                        print(f"{i}. Nama: {teacher['name']}")
                        print(f"   NUPTK: {teacher['nuptk']}")
                        print(f"   Tanggal Lahir: {teacher['dob']}")
                        print(f"   Mata Pelajaran: {', '.join(teacher['subjects'])}")
                        print("-" * 30)
            elif choice == '3':  # Cari Data Guru
                self.clear_screen()
                print("Cari Data Guru")
                print("1. Cari berdasarkan Nama")
                print("2. Cari berdasarkan NUPTK")
                print("3. Cari berdasarkan Tanggal Lahir")
                print("4. Cari berdasarkan Mata Pelajaran")
                search_choice = input("Pilih kriteria pencarian (1-4): ")
                
                if search_choice == '1':
                    key = 'name'
                    value = input("Masukkan Nama: ")
                elif search_choice == '2':
                    key = 'nuptk'
                    value = input("Masukkan NUPTK: ")
                elif search_choice == '3':
                    key = 'dob'
                    value = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
                elif search_choice == '4':
                    # Untuk mata pelajaran, kita perlu pendekatan khusus karena ini adalah list
                    subject = input("Masukkan Mata Pelajaran: ")
                    teachers = self.teacher_manager.get_all_teachers()
                    found = False
                    for teacher in teachers:
                        if subject in teacher['subjects']:
                            print("\nHasil Pencarian:")
                            print(f"Nama: {teacher['name']}")
                            print(f"NUPTK: {teacher['nuptk']}")
                            print(f"Tanggal Lahir: {teacher['dob']}")
                            print(f"Mata Pelajaran: {', '.join(teacher['subjects'])}")
                            found = True
                    
                    if not found:
                        print("Data tidak ditemukan.")
                    
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                result = self.teacher_manager.search_teacher(key, value)
                if result:
                    print("\nHasil Pencarian:")
                    print(f"Nama: {result['name']}")
                    print(f"NUPTK: {result['nuptk']}")
                    print(f"Tanggal Lahir: {result['dob']}")
                    print(f"Mata Pelajaran: {', '.join(result['subjects'])}")
                else:
                    print("Data tidak ditemukan.")
            elif choice == '4':  # Update Data Guru
                self.clear_screen()
                print("Update Data Guru")
                nuptk = input("NUPTK Guru yang akan diupdate: ")
                teacher = self.teacher_manager.get_teacher_by_nuptk(nuptk)
                if not teacher:
                    print("Guru dengan NUPTK tersebut tidak ditemukan.")
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
                        'nuptk': nuptk,
                        'dob': dob,
                        'subjects': subjects,
                        'password': password if password else teacher['password']
                    }
                    self.teacher_manager.update_teacher(nuptk, new_data)
            elif choice == '5':  # Hapus Data Guru
                self.clear_screen()
                print("Hapus Data Guru")
                nuptk = input("NUPTK Guru yang akan dihapus: ")
                confirm = input(f"Anda yakin ingin menghapus guru dengan NUPTK {nuptk}? (y/n): ")
                if confirm.lower() == 'y':
                    self.teacher_manager.delete_teacher(nuptk)
            elif choice == '6':  # Urutkan Data Guru
                self.clear_screen()
                print("Urutkan Data Guru")
                print("1. Urutkan berdasarkan Nama")
                print("2. Urutkan berdasarkan NUPTK")
                print("3. Urutkan berdasarkan Tanggal Lahir")
                print("4. Kembali")
                sort_choice = input("Pilih kriteria pengurutan (1-4): ")
                
                if sort_choice == '1':
                    key = 'name'
                elif sort_choice == '2':
                    key = 'nuptk'
                elif sort_choice == '3':
                    key = 'dob'
                elif sort_choice == '4':
                    continue
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                order_choice = input("Urutkan secara (1) Ascending atau (2) Descending? (1/2): ")
                ascending = True if order_choice == '1' else False
                
                sorted_teachers = self.teacher_manager.sort_teachers(key, ascending)
                
                print("\nHasil Pengurutan:")
                for i, teacher in enumerate(sorted_teachers, 1):
                    print(f"{i}. Nama: {teacher['name']}")
                    print(f"   NUPTK: {teacher['nuptk']}")
                    print(f"   Tanggal Lahir: {teacher['dob']}")
                    print(f"   Mata Pelajaran: {', '.join(teacher['subjects'])}")
                    print("-" * 30)
            elif choice == '0':  # Kembali
                break
            else:
                print("Pilihan tidak valid.")
            
            input("Tekan Enter untuk melanjutkan...")
    
    def manage_reset_password_requests(self):
        while True:
            self.display_reset_password_menu()
            choice = input("Pilih menu (0-3): ")
            
            if choice == '1':  # Lihat Permintaan Pending
                self.clear_screen()
                print("=" * 50)
                print("PERMINTAAN RESET PASSWORD PENDING".center(50))
                print("=" * 50)
                
                pending_requests = self.account_manager.get_pending_reset_requests()
                if not pending_requests:
                    print("Tidak ada permintaan reset password yang pending.")
                else:
                    for i, request in enumerate(pending_requests, 1):
                        print(f"{i}. No: {request['id']}")
                        print(f"   Jenis Pengguna: {request['user_type'].capitalize()}")
                        print(f"   ID Pengguna: {request['user_id']}")
                        print(f"   Password Baru: {request['new_pass']}")
                        print(f"   Tanggal Permintaan: {request['request_date']}")
                        print("-" * 30)
            
            elif choice == '2':  # Lihat Semua Permintaan
                self.clear_screen()
                print("=" * 50)
                print("SEMUA PERMINTAAN RESET PASSWORD".center(50))
                print("=" * 50)
                
                all_requests = self.account_manager.get_all_reset_requests()
                if not all_requests:
                    print("Tidak ada permintaan reset password.")
                else:
                    for i, request in enumerate(all_requests, 1):
                        print(f"{i}. No: {request['id']}")
                        print(f"   Jenis Pengguna: {request['user_type'].capitalize()}")
                        print(f"   ID Pengguna: {request['user_id']}")
                        print(f"   Password Baru: {request['new_pass']}")
                        print(f"   Tanggal Permintaan: {request['request_date']}")
                        print(f"   Status: {request['status'].capitalize()}")
                        if request['processed_date']:
                            print(f"   Tanggal Diproses: {request['processed_date']}")
                        print("-" * 30)
            
            elif choice == '3':  # Proses Permintaan
                self.clear_screen()
                print("=" * 50)
                print("PROSES PERMINTAAN RESET PASSWORD".center(50))
                print("=" * 50)
                
                request_id = input("Masukkan No permintaan: ")
                try:
                    request_id = int(request_id)
                    request = self.account_manager.get_reset_request_by_id(request_id)
                    
                    if not request:
                        print("Permintaan dengan No tersebut tidak ditemukan.")
                    elif request['status'] != 'pending':
                        print(f"Permintaan ini sudah diproses dengan status: {request['status'].capitalize()}")
                    else:
                        print(f"Detail Permintaan:")
                        print(f"No: {request['id']}")
                        print(f"Jenis Pengguna: {request['user_type'].capitalize()}")
                        print(f"ID Pengguna: {request['user_id']}")
                        print(f"Password Baru: {request['new_pass']}")
                        print(f"Tanggal Permintaan: {request['request_date']}")
                        
                        print("\n1. Setujui")
                        print("2. Tolak")
                        print("0. Kembali")
                        action = input("Pilih tindakan (0-2): ")
                        
                        if action == '1':  # Setujui
                            new_password = input("Masukkan password baru: ")
                            self.account_manager.approve_reset_request(request_id)
                            
                            if self.account_manager.reset_password(request['user_type'], request['user_id'], new_password):
                                print("Password berhasil direset.")
                            else:
                                print("Gagal mereset password.")
                        
                        elif action == '2':  # Tolak
                            self.account_manager.reject_reset_request(request_id)
                            print("Permintaan reset password ditolak.")
                
                except ValueError:
                    print("No permintaan harus berupa angka.")
            
            elif choice == '0':  # Kembali
                break
            else:
                print("Pilihan tidak valid.")
            
            input("Tekan Enter untuk melanjutkan...")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Pilih menu (0-4): ")
            
            if choice == '1':  # Manajemen Data Sekolah
                self.manage_school_data()
            elif choice == '2':  # Manajemen Data Siswa
                self.manage_student_data()
            elif choice == '3':  # Manajemen Data Guru
                self.manage_teacher_data()
            elif choice == '4':  # Kelola Permintaan Reset Password
                self.manage_reset_password_requests()
            elif choice == '0':  # Logout
                break
            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan...")
        
        return None  # Mengembalikan None untuk menandakan logout