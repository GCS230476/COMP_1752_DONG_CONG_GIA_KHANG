
import tkinter as tk
from center_creen import center_window
import video_library as lib

class UpdateVideo:
    def __init__(self, window, switch_to_main_screen):
        self.window = window
        self.switch_to_main_screen = switch_to_main_screen
        self.window.geometry("520x520")
        self.window.title("Update Video")
        center_window(self.window, 520, 520)  # Pass the Toplevel window object

        tk.Label(self.window, text="Video Number:").grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.key_entry = tk.Entry(self.window)
        self.key_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.window, text="New Name:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.window, text="New Director:").grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.director_entry = tk.Entry(self.window)
        self.director_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.window, text="New Rating (0-5):").grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.rating_entry = tk.Entry(self.window)
        self.rating_entry.grid(row=3, column=1, padx=10, pady=5)

        update_btn = tk.Button(self.window, text="Update Video", command=self.update_video)
        update_btn.grid(row=4, column=0, columnspan=2, pady=10)

        back_btn = tk.Button(self.window, text="Back to Main", command=self.switch_to_main_screen)
        back_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def update_video(self):
        key = self.key_entry.get()
        name = self.name_entry.get()
        director = self.director_entry.get()
        try:
            rating = int(self.rating_entry.get())
        except ValueError:
            rating = 0

        lib.update_video(key, name=name, director=director, rating=rating)
        tk.messagebox.showinfo("Success", "Video updated successfully!")
