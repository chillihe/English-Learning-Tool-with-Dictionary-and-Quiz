from tkinter import *

LARGE_FONT= ("Verdana", 12)

class StartPage(Frame):

    def __init__(self, parent, controller, btn_dict, btn_quiz):
        Frame.__init__(self,parent, width = 500, height = 500, background = 'bisque')
        self.grid_rowconfigure(0, minsize = 500, weight = 1)
        self.grid_rowconfigure(8, minsize = 500, weight = 1)
        self.grid_columnconfigure(0, minsize = 500, weight = 1)
        self.grid_columnconfigure(8, minsize = 500, weight = 1)

        label1 = Label(self, text="Welcome to my English Learning App", font=LARGE_FONT, width = 50)
        label1.pack(pady=10,padx=10)
        
        button = Button(self, text="Go to Dictionary",
                            command=lambda: controller.show_frame(btn_dict))
        button.pack()

        button2 = Button(self, text="Go to Quiz",
                            command=lambda: controller.show_frame(btn_quiz))
        button2.pack()