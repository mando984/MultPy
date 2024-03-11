"""
On my page, display the table, start, or quit the game.
"""
import sys
from pathlib import Path

# Add the main directory to PYTHONPATH.
main_directory = Path(__file__).resolve().parents[1]
sys.path.append(str(main_directory))

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import*

from data.table import read_rank_list

class MainPage(tk.Frame):
    def __init__(self, next_page_callback):
        super().__init__()

        self.next_page_callback= next_page_callback

        # displays application name on header
        self.header_label = ttk.Label(self, text="MultiPy", font=("Helvetica", 30), foreground="#CA9A07")
        self.header_label.pack(pady=20)

       
        self.list_name = ttk.Label(self, text="RankList", font=("Helvetica", 18), foreground="#CA9A07")
        self.list_name.pack(pady=10)

        #print table
        self.tree = ttk.Treeview(self)

        self.tree["columns"] = ("#", "Name", "Score", "Time")
        self.tree.column("#", width=100, minwidth=50, stretch=tk.NO)
        self.tree.column("Name", width=150, minwidth=50, stretch=tk.NO)
        self.tree.column("Score", width=150, minwidth=50, stretch=tk.NO)
        self.tree.column("Time", width=150, minwidth=50, stretch=tk.NO)

        self.tree.heading("#", text="Place", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Score", text="Score", anchor=tk.W)
        self.tree.heading("Time", text="Time", anchor=tk.W)

        # Set the data in the Treeview
        self.refresh_table()  # Updating the table

        # Set the start_button to move to secund_page
        self.start_button = ttk.Button(self, text=" Start new game ",style= "outline", command=self.next_page_callback)
        self.start_button.pack(pady=30)

        self.quit_button = ttk.Button(self, text="Quit game",  width=14, style= "outline", command=self.quit)
        self.quit_button.pack(pady=10)

        #  every show frame1 call on_show mhetod 
        self.bind("<Visibility>", lambda event: self.on_show(event, self)) 

    def on_show(self, event, widget):
        widget.refresh_table()  # update table 
       # widget.update_idletasks()    
 

       # Updating the table
    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())  # clear table
        #self.tree.update_idletasks()
        players = read_rank_list() 
        for i, player in enumerate(players, start=1):
            self.tree.insert("", "end", values=(i, player["Name"], player["Score"], player["Time"]))    
        self.tree.pack(pady=10)    


    def start_application(self):
        self.mainloop()    


def main():
    next_page_callback = ''
    apps = MainPage(next_page_callback)
    apps.start_application()


if __name__ == "__main__":
    main()
