from tkinter import *
from StartPage import StartPage
from DictionaryPage import DictionaryPage
from QuizPage import QuizPage
import Backend

class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, DictionaryPage, QuizPage):
            button_dict = {StartPage : (DictionaryPage, QuizPage), 
                           DictionaryPage : (StartPage, QuizPage), 
                           QuizPage : (StartPage, DictionaryPage)}

            frame = F(container, self, button_dict[F][0], button_dict[F][1])
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

Backend.connect()
app = SeaofBTCapp()
app.mainloop()
