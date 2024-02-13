import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter


def add_noise():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    noisy_image = image.filter(ImageFilter.GaussianBlur(radius=10))
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    noisy_image.save(save_path)
    tk.messagebox.showinfo("Operation Complete", "Noise added and image saved.")


def remove_noise():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    denoised_image = image.filter(ImageFilter.GaussianBlur(radius=0))
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    denoised_image.save(save_path)
    tk.messagebox.showinfo("Operation Complete", "Noise removed and image saved.")


root = tk.Tk()
root.title("Image Noise Removal")

add_noise_button = tk.Button(root, text="Add Noise", command=add_noise)
add_noise_button.pack(pady=10)

remove_noise_button = tk.Button(root, text="Remove Noise", command=remove_noise)
remove_noise_button.pack(pady=10)

root.mainloop()
