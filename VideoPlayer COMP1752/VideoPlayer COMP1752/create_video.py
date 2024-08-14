
import tkinter as tk
from center_creen import center_window
import video_library as lib

class CreateVideo:
    def __init__(self, window, switch_to_main_screen):
        self.window = window
        self.switch_to_main_screen = switch_to_main_screen
        self.window.geometry("350x200")
        self.window.title("Create Video")
        center_window(self.window, 350, 200)


        tk.Label(self.window, text="Video Name:").grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.window, text="Director:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.director_entry = tk.Entry(self.window)
        self.director_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.window, text="Rating (0-5):").grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.rating_entry = tk.Entry(self.window)
        self.rating_entry.grid(row=2, column=1, padx=10, pady=5)

        submit_btn = tk.Button(self.window, text="Add Video", command=self.add_video)
        submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

        back_btn = tk.Button(self.window, text="Back to Main", command=self.switch_to_main_screen)
        back_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def add_video(self):
        name = self.name_entry.get()
        director = self.director_entry.get()
        try:
            rating = int(self.rating_entry.get())
        except ValueError:
            rating = 0

        lib.add_video(name, director, rating)
        self.name_entry.delete(0, tk.END)
        self.director_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

        tk.messagebox.showinfo("Success", "Video added successfully!")
