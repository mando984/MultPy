import tkinter as tk
from tkinter import ttk

from data.table import read_rank_list, write_rank_list, sort_player


class FourthPage(tk.Frame):
    def __init__(self, next_page_callback):
        super().__init__()
        
        self.next_page_callback = next_page_callback
        
        # displays application name on header
        self.header_label = ttk.Label(self, text="MultiPy", font=("Helvetica", 30), foreground="#CA9A07")
        self.header_label.pack(pady=20)

        # Display users score
        self.total_score_label = ttk.Label(self, text="", font=("Helvetica", 20), foreground="#CA9A07")
        self.total_score_label.pack(pady=30)

        # Display users time
        self.total_time_label = ttk.Label(self, text="",font=("Helvetica", 20), foreground="#CA9A07")
        self.total_time_label.pack(pady=10, padx=50)

        # Frame for user's name input
        name_frame = ttk.Frame(self)
        name_frame.pack(pady=50)

        self.name_label = ttk.Label(name_frame, text="Enter your name:")
        self.name_label.pack(side=tk.LEFT)

        self.name_entry = ttk.Entry(name_frame)
        self.name_entry.pack(side=tk.LEFT, padx=10)
        self.name_entry.focus()
        self.name_entry.bind('<Return>', self.player_name) # when press Enter value will be forwarded
       
        
    # This instance get from ThirdPage throw project.py
    def init_score_instance(self,score_instance):
        self.score = score_instance
        self.total_score_label.config( text=f"Congratulation ! your score is {self.score.score}")  
        self.total_time_label.config( text=f"Your time is {self.score.time}") 
        self.name_entry.focus()
        

    def player_name(self, event=None):
        name = self.name_entry.get()
        name = self.valid_name(name)
        if name:
            self.add_player(name)
            self.name_entry.delete(0, tk.END)
            self.next_page_callback()


    def valid_name(self, name):
        if name == "":
            name = "Player"
        return name.capitalize()     


    # Add  new player to csv file
    def add_player(self, name):
        players = read_rank_list()
        new_player = {"Name": name, "Score": int(self.score.score), "Time": int(self.score.time)}
        players.append(new_player)
        sorted_players = sort_player(players)
        write_rank_list(sorted_players)
       

       