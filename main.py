import os
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Konfigurasi folder utama dan tujuan
MAIN_FOLDER = "photos"
SORTED_FOLDERS = ["folder1", "folder2", "folder3", "folder4", "folder5"]
DELETE_FOLDER = "deleted"

# Pastikan folder tujuan ada
for folder in SORTED_FOLDERS + [DELETE_FOLDER]:
    os.makedirs(folder, exist_ok=True)

def get_photos():
    return [f for f in os.listdir(MAIN_FOLDER) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

class PhotoSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Sorter")

        self.photos = get_photos()
        self.current_index = 0
        
        self.img_label = tk.Label(root)
        self.img_label.pack()
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Tombol Delete
        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_photo, bg="red", fg="white")
        self.delete_button.grid(row=0, column=0)

        # Tombol Folder
        self.folder_buttons = []
        for i, folder in enumerate(SORTED_FOLDERS):
            btn = tk.Button(self.button_frame, text=f"Folder {i+1}", command=lambda f=folder: self.move_photo(f))
            btn.grid(row=0, column=i+1)
            self.folder_buttons.append(btn)

        self.load_photo()

    def load_photo(self):
        if self.current_index < len(self.photos):
            img_path = os.path.join(MAIN_FOLDER, self.photos[self.current_index])
            img = Image.open(img_path)
            img = img.resize((400, 400))
            self.tk_img = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.tk_img)
        else:
            self.img_label.config(image="", text="No more photos")

    def move_photo(self, folder):
        if self.current_index < len(self.photos):
            src = os.path.join(MAIN_FOLDER, self.photos[self.current_index])
            dst = os.path.join(folder, self.photos[self.current_index])
            shutil.move(src, dst)
            self.current_index += 1
            self.load_photo()

    def delete_photo(self):
        if self.current_index < len(self.photos):
            src = os.path.join(MAIN_FOLDER, self.photos[self.current_index])
            dst = os.path.join(DELETE_FOLDER, self.photos[self.current_index])
            shutil.move(src, dst)
            self.current_index += 1
            self.load_photo()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoSorterApp(root)
    root.mainloop()
