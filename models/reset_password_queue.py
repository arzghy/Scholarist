# models/reset_password_queue.py
# Kelas untuk mengelola antrean permintaan reset password

import json
import os
from datetime import datetime

class ResetPasswordQueue:
    def __init__(self):
        self.filename = 'reset_password_queue.json'
        self.queue = []
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.queue = json.load(file)
            except json.JSONDecodeError:
                print(f"Error: File {self.filename} tidak valid.")
                self.queue = []
        else:
            # Buat file baru jika belum ada
            with open(self.filename, 'w') as file:
                json.dump([], file)
    
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.queue, file, indent=4)
    
    def add_request(self, user_type, user_id, new_pass):
        """
        Menambahkan permintaan reset password ke antrean
        
        Args:
            user_type (str): Jenis pengguna ('guru', 'siswa', 'operator')
            user_id (str): ID pengguna (NUPTK, NISN, atau username)
            reason (str): Alasan permintaan reset password
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        # Cek apakah permintaan sudah ada dalam antrean
        for request in self.queue:
            if request['user_type'] == user_type and request['user_id'] == user_id and request['status'] == 'pending':
                return False
        
        # Tambahkan permintaan baru
        request = {
            'id': len(self.queue) + 1,
            'user_type': user_type,
            'user_id': user_id,
            'new_pass': new_pass,
            'request_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'pending',
            'processed_date': None
        }
        
        self.queue.append(request)
        self.save_data()
        return True
    
    def get_pending_requests(self):
        """
        Mendapatkan semua permintaan yang masih pending
        
        Returns:
            list: Daftar permintaan yang masih pending
        """
        return [request for request in self.queue if request['status'] == 'pending']
    
    def get_all_requests(self):
        """
        Mendapatkan semua permintaan
        
        Returns:
            list: Daftar semua permintaan
        """
        return self.queue
    
    def approve_request(self, request_id):
        """
        Menyetujui permintaan reset password
        
        Args:
            request_id (int): ID permintaan
        
        Returns:
            dict: Data permintaan yang disetujui, None jika tidak ditemukan
        """
        for request in self.queue:
            if request['id'] == request_id and request['status'] == 'pending':
                request['status'] = 'Disetujui'
                request['processed_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_data()
                return request
        return None
    
    def reject_request(self, request_id):
        """
        Menolak permintaan reset password
        
        Args:
            request_id (int): ID permintaan
        
        Returns:
            dict: Data permintaan yang ditolak, None jika tidak ditemukan
        """
        for request in self.queue:
            if request['id'] == request_id and request['status'] == 'pending':
                request['status'] = 'Ditolak'
                request['processed_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_data()
                return request
        return None
    
    def get_request_by_id(self, request_id):
        """
        Mendapatkan permintaan berdasarkan ID
        
        Args:
            request_id (int): ID permintaan
        
        Returns:
            dict: Data permintaan, None jika tidak ditemukan
        """
        for request in self.queue:
            if request['id'] == request_id:
                return request
        return None
    
    def get_user_pending_request(self, user_type, user_id):
        """
        Mendapatkan permintaan pending dari pengguna tertentu
        
        Args:
            user_type (str): Jenis pengguna ('guru', 'siswa', 'operator')
            user_id (str): ID pengguna (NUPTK, NISN, atau username)
        
        Returns:
            dict: Data permintaan, None jika tidak ditemukan
        """
        for request in self.queue:
            if request['user_type'] == user_type and request['user_id'] == user_id and request['status'] == 'pending':
                return request
        return None