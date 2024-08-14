
import tkinter as tk
import font_manager as fonts
from center_creen import center_window
from check_videos import CheckVideos


class MainScreen():
    def __init__(self, window, switch_to_check_videos, switch_to_create_video, show_update_video_screen):
        self.window = window
        self.switch_to_check_videos = switch_to_check_videos
        self.switch_to_create_video = switch_to_create_video
        self.show_update_video_screen = show_update_video_screen

        center_window(self.window, 750, 150)

        window.title("Videos Player")
        label = tk.Label(window, text="Select an option by clicking one of the buttons below")
        label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        check_button = tk.Button(window, text="Check Videos", command=self.switch_to_check_videos)
        check_button.grid(row=1, column=0, padx=10, pady=10)

        create_button = tk.Button(window, text="Create Video List", command=self.switch_to_create_video)
        create_button.grid(row=1, column=1, padx=10, pady=10)

        update_button = tk.Button(window, text="Update Videos", command=self.show_update_video_screen)
        update_button.grid(row=1, column=2, padx=10, pady=10)

        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        window.grid_columnconfigure(2, weight=1)
