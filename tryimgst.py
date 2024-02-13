from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
from cryptography.fernet import Fernet
import base64
import tkinter as tk
from tkinter import messagebox

root = Tk()
root.title("Steganography - Hide Text in msg")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

bg_image = ImageTk.PhotoImage(Image.open("CRYPTOGRAPHY PROJECT.png"))
bg_image1 = ImageTk.PhotoImage(Image.open("Enter-2.png"))
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File')

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img


def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)
    text1.delete(1.0, END)


def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


def save():
    secret.save("hidden.png")

def encrypt_data(key, data):
    # Create a Fernet cipher object with the given key
    cipher = Fernet(key)

    # Encrypt the data
    encrypted_data = cipher.encrypt(data.encode('utf-8'))

    # Base64 encode the encrypted data
    encrypted_data_base64 = base64.b64encode(encrypted_data)

    return encrypted_data_base64.decode('utf-8')

def decrypt_data(key, encrypted_data):
    # Create a Fernet cipher object with the given key
    cipher = Fernet(key)

    # Base64 decode the encrypted data
    encrypted_data_bytes = base64.b64decode(encrypted_data)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data_bytes)

    return decrypted_data.decode('utf-8')


def encrypt_button_click():
    encryption_window = tk.Toplevel(root)
    encryption_window.title("AES Encryption")
    bg_label1 = Label(encryption_window, image=bg_image1)
    bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
    key_label = tk.Label(encryption_window, text="Enter the encryption key:")
    key_label.pack()
    key_entry = tk.Entry(encryption_window, show="*")
    key_entry.pack()

    data_label = tk.Label(encryption_window, text="Enter the data to encrypt:")
    data_label.pack()
    data_entry = tk.Text(encryption_window, height=5)
    data_entry.pack()

    def perform_encryption():
        key = key_entry.get()
        data = data_entry.get("1.0", "end-1c")

        if not key:
            messagebox.showerror("Empty Key", "Please enter the encryption key.")
            return

        if not data:
            messagebox.showerror("Empty Data", "Please enter the data to encrypt.")
            return

        encrypted_data = encrypt_data(key, data)
        messagebox.showinfo("Encryption Result", f"Encrypted data:\n{encrypted_data}")

    encrypt_button = tk.Button(encryption_window, text="Encrypt", command=perform_encryption)
    encrypt_button.pack()


def decrypt_button_click():
    decryption_window = tk.Toplevel(root)
    decryption_window.title("AES Decryption")
    bg_label2 = Label(decryption_window, image=bg_image1)
    bg_label2.place(x=0, y=0, relwidth=1, relheight=1)
    key_label = tk.Label(decryption_window, text="Enter the encryption key:")
    key_label.pack()
    key_entry = tk.Entry(decryption_window, show="*")
    key_entry.pack()

    data_label = tk.Label(decryption_window, text="Enter the data to decrypt:")
    data_label.pack()
    data_entry = tk.Text(decryption_window, height=5)
    data_entry.pack()

    def perform_decryption():
        key = key_entry.get()
        encrypted_data = data_entry.get("1.0", "end-1c")

        if not key:
            messagebox.showerror("Empty Key", "Please enter the encryption key.")
            return

        if not encrypted_data:
            messagebox.showerror("Empty Data", "Please enter the data to decrypt.")
            return

        decrypted_data = decrypt_data(key, encrypted_data)
        messagebox.showinfo("Decryption Result", f"Decrypted data:\n{decrypted_data}")

    decrypt_button = tk.Button(decryption_window, text="Decrypt", command=perform_decryption)
    decrypt_button.pack()


# icon
#image_icon = PhotoImage(file="GameXertZ.png")
#root.iconphoto(False, image_icon)

# logo
# logo=PhotoImage(file="GameXertZ.png")
# Label(root,image=logo,bg="#2f4155").place(x=10,y=0)

#Label(root, text="Cryptography Project", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# first frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)
lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# second frame
frame2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=328, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third Frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# fourth Frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

font_style = ("Blanka-Regular.otf", 12)
Button(frame4, text="Hide Data", width=5, height=2, font="arial 13 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Encryption", width=5, height=2, font="arial 13 bold", command=encrypt_button_click).place(x=91, y=30)
Button(frame4, text="Decryption", width=5, height=2, font="arial 13 bold", command=decrypt_button_click).place(x=164, y=30)
Button(frame4, text="Show Data", width=5, height=2, font="arial 13 bold", command=Show).place(x=236, y=30)
Label(frame4, text="Picture, Image, Photo File", font=font_style, bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()