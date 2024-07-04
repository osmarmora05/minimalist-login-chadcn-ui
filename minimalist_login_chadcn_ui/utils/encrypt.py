from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('CRYPTOGRAPHY_KEY').encode()
f = Fernet(key)

def password_encrypt(password: str) -> str:
    token = f.encrypt(password.encode())
    return token.decode()

def decrypt_password(password: str) -> str:
    decrypted_password = f.decrypt(password.encode()).decode()
    return decrypted_password