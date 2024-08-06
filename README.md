# IMG_Steganography
Cryptography Project
The above Files are attempts on creating a Image steganography

Image steganography and AES encryption are two powerful techniques used to ensure secure communication in various fields. Image steganography involves hiding secret information within an image, while AES encryption is a symmetric-key block cipher that encrypts data to prevent unauthorized access. The combination of these two techniques provides an additional layer of security, making it extremely difficult for unauthorized parties to intercept and decode sensitive information.

Image Steganography and AES Encryption: A Powerful Combination

<img width="1078" alt="image" src="https://github.com/user-attachments/assets/31af7ea1-802a-4d7e-bcd4-6c09b7b10060">


Real-World Examples
Secure Military Communication: Image steganography can be used to hide secret messages within images, which are then encrypted using AES encryption. This ensures that even if the image is intercepted, the encrypted message remains secure.
Digital Forensics: Steganography can be used to hide digital evidence, such as fingerprints or DNA profiles, within images. AES encryption can then be used to protect the evidence from tampering or unauthorized access.
Secure Online Transactions: AES encryption can be used to encrypt sensitive information, such as credit card numbers, while image steganography can be used to hide the encrypted data within an image.

# AIM:
To build a GUI which has options to encrypt/decrypt or to hide some info in a image 
there should be buttons for opening an image and options to encrypt, decrypt and induce some noise in the image.
The end result should be the data recieved on the other end.

# Steps:
open a image -> click encryption -> Write your data and input AES key -> Copy the encryption and past on blank side of Main interface -> Click hide data -> hidden.png {should be downloaded with the data}

Close and Open Application again:-    

open hidden.png -> Click show data -> click decryption -> copy past the encryption and key -> should display the exact data.

# INFO:
encryption_key.txt - has the template for the 256 bit AES key
imagest.py is the latest working code (noise part is not working)

# OUTPUTS:

<img width="699" alt="Screenshot 2024-08-06 at 11 52 41 AM" src="https://github.com/user-attachments/assets/c6d5b54a-8c7b-4ee9-a24a-e8bbf2df625e">
<img width="567" alt="Screenshot 2024-08-06 at 11 51 17 AM" src="https://github.com/user-attachments/assets/14bff96b-51bf-4eb9-925a-2495d9c93ec5">
<img width="253" alt="Screenshot 2024-08-06 at 11 52 15 AM" src="https://github.com/user-attachments/assets/b90bf358-13d3-4c8c-97fa-a4318b4fb073">
<img width="571" alt="Screenshot 2024-08-06 at 11 55 04 AM" src="https://github.com/user-attachments/assets/5431e28c-85df-409c-868f-77b3fbc9d6cc">
<img width="252" alt="Screenshot 2024-08-06 at 11 55 25 AM" src="https://github.com/user-attachments/assets/5338d87f-d5c3-4cef-b8f9-b15cdc996f07">
