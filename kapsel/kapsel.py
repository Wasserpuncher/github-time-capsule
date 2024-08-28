import os
import json
import base64
import hashlib
from cryptography.fernet import Fernet
from datetime import datetime

class Zeitkapsel:
    def __init__(self, date_to_open, kapsel_name, secret_key=None):
        self.date_to_open = datetime.strptime(date_to_open, '%Y-%m-%d')
        self.kapsel_name = kapsel_name
        self.secret_key = secret_key or Fernet.generate_key()
        self.fernet = Fernet(self.secret_key)
        self.is_sealed = False

    def versiegeln(self, data):
        if datetime.now() >= self.date_to_open:
            raise ValueError("Das Öffnungsdatum liegt in der Vergangenheit.")
        if self.is_sealed:
            raise ValueError("Die Zeitkapsel ist bereits versiegelt.")
        
        data_json = json.dumps(data).encode()
        encrypted_data = self.fernet.encrypt(data_json)
        with open(self.kapsel_name, 'wb') as kapsel_file:
            kapsel_file.write(encrypted_data)
        self.is_sealed = True

    def oeffnen(self):
        if datetime.now() < self.date_to_open:
            raise ValueError("Es ist noch nicht Zeit, die Kapsel zu öffnen.")
        
        with open(self.kapsel_name, 'rb') as kapsel_file:
            encrypted_data = kapsel_file.read()
        decrypted_data = self.fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

    def get_secret_key(self):
        return base64.urlsafe_b64encode(self.secret_key).decode()

