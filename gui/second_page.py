"""
On the second page, select the difficulty level and return the value to the Application.
"""

import tkinter as tk
from tkinter import ttk


class SecondPage(tk.Frame):
    def __init__(self, next_page_callback):
        super().__init__()
        self.next_page_callback= next_page_callback
       

        
        self.label = ttk.Label(self, text="Choose difficulty!", font=("Helvetica", 24), foreground="#CA9A07")
        self.label.pack(pady=20)

        self.difficulty_var = tk.StringVar()

        self.easy_button = ttk.Radiobutton(self, text="Easy", variable=self.difficulty_var, value="Easy", command=self.difficulty_changed)
        self.easy_button.pack(pady=20, padx=50)

        self.medium_button = ttk.Radiobutton(self, text="Medium", variable=self.difficulty_var, value="Medium", command=self.difficulty_changed)
        self.medium_button.pack(pady=20, padx=50)

        self.hard_button = ttk.Radiobutton(self, text="Hard", variable=self.difficulty_var, value="Hard", command=self.difficulty_changed)
        self.hard_button.pack(pady=20, padx=50)

        self.next_button = ttk.Button(self, text="Next", width=25, style="outline", command=self.next_button_callback)
        self.next_button.pack(pady=60)
        self.next_button.config(state="disabled")

    
    def difficulty_changed(self):
        if self.difficulty_var.get():
            self.next_button.config(state='normal')  # Enable the Next button
    

    def next_button_callback(self):
        self.difficulty_var.get()
        self.next_page_callback(difficulty_updated=True)


