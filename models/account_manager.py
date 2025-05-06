# models/account_manager.py
# Kelas untuk manajemen akun

from models.json_manager import JSONManager
from models.student_manager import StudentManager
from models.teacher_manager import TeacherManager
from models.reset_password_queue import ResetPasswordQueue

class AccountManager:
    def __init__(self):
        self.admin_manager = JSONManager('admin_data.json')
        self.operator_manager = JSONManager('operator_data.json')
        self.student_manager = StudentManager()
        self.teacher_manager = TeacherManager()
        self.reset_password_queue = ResetPasswordQueue()
    
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
    
    # Fungsi-fungsi untuk antrean reset password
    def request_reset_password(self, user_type, user_id, reason):
        """
        Mengirim permintaan reset password
        
        Args:
            user_type (str): Jenis pengguna ('guru', 'siswa', 'operator')
            user_id (str): ID pengguna (NUPTK, NISN, atau username)
            reason (str): Alasan permintaan reset password
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        return self.reset_password_queue.add_request(user_type, user_id, reason)
    
    def get_pending_reset_requests(self):
        """
        Mendapatkan semua permintaan reset password yang masih pending
        
        Returns:
            list: Daftar permintaan yang masih pending
        """
        return self.reset_password_queue.get_pending_requests()
    
    def get_all_reset_requests(self):
        """
        Mendapatkan semua permintaan reset password
        
        Returns:
            list: Daftar semua permintaan
        """
        return self.reset_password_queue.get_all_requests()
    
    def approve_reset_request(self, request_id):
        """
        Menyetujui permintaan reset password
        
        Args:
            request_id (int): ID permintaan
        
        Returns:
            dict: Data permintaan yang disetujui, None jika tidak ditemukan
        """
        return self.reset_password_queue.approve_request(request_id)
    
    def reject_reset_request(self, request_id):
        """
        Menolak permintaan reset password
        
        Args:
            request_id (int): ID permintaan
        
        Returns:
            dict: Data permintaan yang ditolak, None jika tidak ditemukan
        """
        return self.reset_password_queue.reject_request(request_id)
    
    def get_reset_request_by_id(self, request_id):
        """
        Mendapatkan permintaan reset password berdasarkan ID
        
        Args:
            request_id (int): ID permintaan
        
        Returns:
            dict: Data permintaan, None jika tidak ditemukan
        """
        return self.reset_password_queue.get_request_by_id(request_id)
    
    def get_user_pending_reset_request(self, user_type, user_id):
        """
        Mendapatkan permintaan reset password pending dari pengguna tertentu
        
        Args:
            user_type (str): Jenis pengguna ('guru', 'siswa', 'operator')
            user_id (str): ID pengguna (NUPTK, NISN, atau username)
        
        Returns:
            dict: Data permintaan, None jika tidak ditemukan
        """
        return self.reset_password_queue.get_user_pending_request(user_type, user_id)
    
    def reset_password(self, user_type, user_id, new_password):
        """
        Reset password pengguna
        
        Args:
            user_type (str): Jenis pengguna ('admin', 'guru', 'siswa', 'operator')
            user_id (str): ID pengguna (username, NUPTK, NISN)
            new_password (str): Password baru
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        if user_type == 'admin':
            admin_data = self.admin_manager.get_all()
            for admin in admin_data:
                if admin['username'] == user_id:
                    admin['password'] = new_password
                    self.admin_manager.save_data()
                    return True
        elif user_type == 'guru':
            teacher_data = self.teacher_manager.get_all_teachers()
            for teacher in teacher_data:
                if teacher['nuptk'] == user_id:
                    teacher['password'] = new_password
                    self.teacher_manager.data_manager.save_data()
                    return True
        elif user_type == 'siswa':
            student_data = self.student_manager.get_all_students()
            for student in student_data:
                if student['nisn'] == user_id:
                    student['password'] = new_password
                    self.student_manager.data_manager.save_data()
                    return True
        elif user_type == 'operator':
            operator_data = self.operator_manager.get_all()
            for operator in operator_data:
                if operator['username'] == user_id:
                    operator['password'] = new_password
                    self.operator_manager.save_data()
                    return True
        
        return False