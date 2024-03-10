"""
Here, play the game. There are several connections with project.py.
"""

import tkinter as tk
from tkinter import ttk

class ThirdPage(tk.Frame):
    def __init__(self, next_page_callback, start_level_callback):
        super().__init__()
    
        self.next_page_callback= next_page_callback
        self.start_level_callback = start_level_callback

        self.current_level = 1
        self.answer_var = tk.StringVar()
        self.size_text = 12

        
        # displays application name on header
        self.header_label = ttk.Label(self, text="MultiPy", font=("Helvetica", 30), foreground="#CA9A07")
        self.header_label.grid(row=0, column=0, columnspan= 3, pady=20)
        
        # displays current level on screen
        self.level_label = ttk.Label(self, text="", font=("Helvetica", 18), foreground="#CA9A07")
        self.level_label.grid(row=1,column=0, columnspan=3, pady=40)

        # run level 
        self.start_button = ttk.Button(self, text=f"Start level {self.current_level}", width=25, style="outline",  command=self.start_level_callback)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=20)
    
        # group element for quest, answer and help
        self.quest_frame = ttk.Frame(self)
        self.quest_frame.grid(row=3, column=0 , columnspan=3, pady=10)
        self.quest_frame.grid_forget() 
        
        #show quest
        self.quest_label = ttk.Label(self.quest_frame, text="", font=("Helvetica", 16))
        self.quest_label.grid(row=0, column=0, sticky="w", padx=10)
       
        #user input answre
        self.answer_entry = ttk.Entry(self.quest_frame, textvariable=self.answer_var, font=("Helvetica", 12), width=6)
        self.answer_entry.grid(row=0, column=1, sticky="w", padx=10)
        self.answer_entry.grid_forget()

        # show hint 
        self.help_label = ttk.Label(self.quest_frame, text="", font=("Helvetica", 12), foreground="#CA9A07")
        self.help_label.grid(row=1, column=0, columnspan=2, pady=15)

        # swow if answer correct or not
        self.feedback_result_label = ttk.Label(self, text="", font=("Helvetica", 24))
        self.feedback_result_label.grid(row=4, column=0, columnspan=3, pady=10)
        
        # show current combo on display
        self.combo_frame = ttk.Frame(self)
        self.combo_frame.grid(row=5, column=0, sticky="sw", pady=90, ipadx=50)

        self.combo_print_label = ttk.Label(self.combo_frame, text="Combo  x", font=("Helvetica", self.size_text ))
        self.combo_print_label.grid(row=0, column=0)

        self.combo_number_label = ttk.Label(self.combo_frame, text="1", font=("Helvetica", self.size_text))
        self.combo_number_label.grid(row=0, column=1, padx=5)

        #show user current score
        self.score_frame = ttk.Frame(self)
        self.score_frame.grid(row=5, column=2, sticky="se", pady=90, padx=50)

        self.score_print_label = ttk.Label(self.score_frame, text="Score =", font=("Helvetica", 12))
        self.score_print_label.grid(row=0, column=0)

        self.score_number_label = ttk.Label(self.score_frame, text="0", font=("Helvetica", 12))
        self.score_number_label.grid(row=0, column=1)
    