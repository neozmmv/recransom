import os
import pyaes

def decrypt_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.EXTENSION'):
                with open(file_path, "rb") as f:
                    file_data = f.read()

                aes = pyaes.AESModeOfOperationCTR(key.encode())

                # Decrypt file data
                decrypted_data = aes.decrypt(file_data)

                # Remove file extension
                new_file_name = file[:-11] #CHANGE THE 11 (extension lenght) accordingly with your encrypted file extension

                # Write decrypted data back to file with original name
                with open(file_path[:-11], "wb") as f: #CHANGE THE 11 (extension lenght) accordingly with your encrypted file extension
                    f.write(decrypted_data)

                # Remove encrypted file
                os.remove(file_path)

# Your decryption key (same used on encryption)
key = "INSERT KEY HERE"

# Directory to decrypt
directory_to_decrypt = 'INSERT DIRECTORY PATH HERE'

# Decrypt files recursively in the directory
decrypt_files_in_directory(directory_to_decrypt, key)
