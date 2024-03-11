"""
Applications are the controllers for manipulating pages.
The application instance's score after the second page has been completed.

"""

import sys
from pathlib import Path

# Add the main directory to PYTHONPATH.
main_directory = Path(__file__).resolve().parents[1]
sys.path.append(str(main_directory))

import tkinter as tk 
from tkinter import ttk
from ttkbootstrap import*

from gui.main_page import MainPage
from gui.second_page import SecondPage
from gui.third_page import ThirdPage
from gui.fourth_page import FourthPage

from data.score import Score


class Application(tk.Tk):
    def __init__(self, start_level_callback):
        super().__init__()
      
        self._difficulty = ""
        self.title("MultiPy")
        self.geometry("800x600")
        self.style = Style(theme='solar')
       
        self.start_level_callback = start_level_callback
        self.score = None
    
        # every frame have instance for take and addition value to Aplication atribute
        self.frame1 = MainPage(self.show_frame2)
        self.frame1.pack()
        self.frame2 = SecondPage(self.show_frame3)
        self.frame3 = ThirdPage(self.show_frame4, self.start_level_callback)
        self.frame4 = FourthPage(self.show_frame1)


    def show_frame2(self):
        self.frame1.forget()
        self.frame2.tkraise()
        self.frame2.pack()


    def show_frame3(self, difficulty_updated=False):  
        self.frame2.forget()
        self.frame3.tkraise()
        if difficulty_updated:   # if in frame_2 change difficulty
            self.init_score() # then in frame_3 active method for initializatin instance Score
            self.frame3.pack()


    def show_frame4(self):
        self.style = Style(theme='solar')
        self.frame3.forget()
        self.frame4.tkraise()
        self.frame4.pack()
    

    def show_frame1(self):
        self.reset_frames()
        self.frame1 = MainPage(self.show_frame2)
        self.frame1.pack()
        self.frame2 = SecondPage(self.show_frame3)
        self.frame3 = ThirdPage(self.show_frame4, self.start_level_callback)
        self.frame4 = FourthPage(self.show_frame1)


    # destroy all frame to allow new game
    def reset_frames(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        

    @property
    def difficulty(self):
        return self._difficulty
    

    @property
    def game_in_progress(self):
        return self.level_in_progress


    @game_in_progress.setter
    def game_in_progress(self, value):
        self.level_in_progress = value


    def init_score(self):
        self._difficulty = self.frame2.difficulty_var.get()
        self.score = Score(self._difficulty)


    def score_instance(self):
        if self.score != None:
            return self.score
        
        
    def start_application(self):
        self.mainloop()    

