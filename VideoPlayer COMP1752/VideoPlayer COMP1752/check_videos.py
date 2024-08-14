import tkinter as tk  # Import the tkinter library for creating GUI applications
from tkinter import messagebox  # Import messagebox for displaying popup messages
import tkinter.scrolledtext as tkst  # Import scrolled text for creating scrollable text areas
import video_library as lib  # Import the video_library module for video data management
import font_manager as fonts  # Import font_manager for setting up font configurations
from center_creen import center_window  # Import center_window function to center the GUI window
from utils import set_text  # Import set_text function to insert text into a text widget

class CheckVideos:
    def __init__(self, window, switch_to_main_screen):
        self.window = window  # Store the window instance for later use
        self.switch_to_main_screen = switch_to_main_screen  # Store the callback to switch back to the main screen
        self.window.geometry("750x460")  # Set the window size to 750x460 pixels
        self.window.title("Check Videos")  # Set the title of the window
        fonts.configure()  # Apply font settings from the font_manager module

        # Center the window on the screen
        center_window(self.window, 750, 460)

        # Button to list all videos
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label and entry to input a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry box to input a video number, width of 3 characters
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to check details of a specific video by its number
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # Label and entry to filter videos by director's name
        filter_lbl = tk.Label(window, text="Filter by Director:")
        filter_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="E")

        # Entry box to input the director's name for filtering, width of 20 characters
        self.filter_entry = tk.Entry(window, width=20)
        self.filter_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to filter videos by director's name
        filter_btn = tk.Button(window, text="Filter", command=self.filter_videos)
        filter_btn.grid(row=1, column=2, padx=10, pady=10)

        # Label and entry to search for videos by name or director
        search_lbl = tk.Label(window, text="Search by Name:")
        search_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="E")

        # Entry box to input the search term (name or director), width of 20 characters
        self.search_entry = tk.Entry(window, width=20)
        self.search_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button to search for videos by name or director
        search_btn = tk.Button(window, text="Search", command=self.search_videos)
        search_btn.grid(row=2, column=2, padx=10, pady=10)

        # Label and entry for searching videos by rating range
        rating_search_lbl = tk.Label(window, text="Search by Rating:")
        rating_search_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="E")

        # Entry box to input the minimum rating for searching, width of 5 characters
        self.min_rating_entry = tk.Entry(window, width=5)
        self.min_rating_entry.grid(row=3, column=1, padx=5, pady=10, sticky="W")

        # Entry box to input the maximum rating for searching, width of 5 characters
        self.max_rating_entry = tk.Entry(window, width=5)
        self.max_rating_entry.grid(row=3, column=1, padx=5, pady=10, sticky="E")

        # Button to search videos by the specified rating range
        rating_search_btn = tk.Button(window, text="Search", command=self.search_videos_by_rating)
        rating_search_btn.grid(row=3, column=2, padx=10, pady=10)

        # ScrolledText widget to display the list of videos, 48 characters wide and 12 lines tall
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=4, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Text widget to display details of a specific video, 24 characters wide and 4 lines tall
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=4, column=4, sticky="NW", padx=10, pady=10)

        # Status label to display messages and feedback to the user
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        # Button to go back to the main screen
        back_button = tk.Button(window, text="Back to Main", command=self.switch_to_main_screen)
        back_button.grid(row=6, column=0, padx=10, pady=10)

        # Automatically list all videos when the screen is initialized
        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_txt.get()  # Get the video number entered by the user
        name = lib.get_name(key)  # Retrieve the video name using the video number
        if name is not None:  # If the video exists
            director = lib.get_director(key)  # Retrieve the director's name
            rating = lib.get_rating(key)  # Retrieve the video rating
            play_count = lib.get_play_count(key)  # Retrieve the play count
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"  # Format the details
            set_text(self.video_txt, video_details)  # Display the details in the video text box
        else:
            set_text(self.video_txt, f"Video {key} not found")  # If video not found, display an error message
        self.status_lbl.configure(text="Check Video button was clicked!")  # Update the status label

    def list_videos_clicked(self):
        video_list = lib.list_all()  # Retrieve the list of all videos
        set_text(self.list_txt, video_list)  # Display the video list in the list text box
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status label

    def filter_videos(self):
        director_name = self.filter_entry.get()  # Get the director's name entered by the user
        if director_name:  # If the director's name is not empty
            filtered_videos = lib.filter_by_director(director_name)  # Filter videos by the director's name
            set_text(self.list_txt, filtered_videos)  # Display the filtered video list
            if not filtered_videos:  # If no videos were found for the director
                self.status_lbl.configure(text=f"No videos found for director: {director_name}")  # Display an error message
            else:
                self.status_lbl.configure(text="Filter applied successfully!")  # Display success message
        else:
            self.status_lbl.configure(text="Please enter a director's name to filter.")  # Prompt the user to enter a director's name

    def search_videos(self):
        search_term = self.search_entry.get()  # Get the search term entered by the user
        if search_term:  # If the search term is not empty
            search_results = lib.search_by_name(search_term)  # Search for videos by name or director
            set_text(self.list_txt, search_results)  # Display the search results
            if not search_results:  # If no videos were found for the search term
                self.status_lbl.configure(text=f"No results found for: {search_term}")  # Display an error message
            else:
                self.status_lbl.configure(text="Search completed successfully!")  # Display success message
        else:
            self.status_lbl.configure(text="Please enter a search term.")  # Prompt the user to enter a search term

    def search_videos_by_rating(self):
        try:
            min_rating = int(self.min_rating_entry.get())  # Get the minimum rating entered by the user
            max_rating = int(self.max_rating_entry.get())  # Get the maximum rating entered by the user
            if 0 <= min_rating <= max_rating <= 5:  # Validate the rating range (must be between 0 and 5)
                search_results = lib.search_by_rating(min_rating, max_rating)  # Search for videos within the rating range
                set_text(self.list_txt, search_results)  # Display the search results
                if not search_results:  # If no videos were found for the rating range
                    self.status_lbl.configure(text=f"No results found for ratings between {min_rating} and {max_rating}")  # Display an error message
                else:
                    self.status_lbl.configure(text="Search by rating completed successfully!")  # Display success message
            else:
                self.status_lbl.configure(text="Please enter valid ratings between 0 and 5.")  # Prompt the user to enter a valid rating range
        except ValueError:  # If the user entered non-numeric values
            self.status_lbl.configure(text="Please enter valid numeric ratings.")  # Prompt the user to enter numeric ratings
