import tkinter as tk

from create_video import CreateVideo
from main_screen import MainScreen
from check_videos import CheckVideos
import font_manager as fonts
from update_video import UpdateVideo


class App():
    def __init__(self, window):
        self.window = window
        self.show_main_screen()

    def show_main_screen(self):
        self.clear_window()
        MainScreen(self.window, self.show_check_videos, self.show_create_video_screen,self.show_update_video_screen)

    def show_check_videos(self):
        self.clear_window()
        CheckVideos(tk.Toplevel(self.window), self.show_main_screen)

    def show_create_video_screen(self):
        self.clear_window()
        CreateVideo(tk.Toplevel(self.window), self.show_main_screen)

    def show_update_video_screen(self):
        self.clear_window()
        UpdateVideo(tk.Toplevel(self.window), self.show_main_screen)

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    app = App(window)
    window.mainloop()
