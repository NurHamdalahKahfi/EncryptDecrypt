from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

with open('20190801162-Nur_Hamdalah_Kahfi.txt','rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open('20190801162-Nur_Hamdalah_Kahfi.txt.decrypted', 'wb') as f: 
    f.write(encrypted)
