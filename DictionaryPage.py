from tkinter import *
from tkinter import messagebox
import Backend

LARGE_FONT= ("Verdana", 12)

class DictionaryPage(Frame):

    def __init__(self, parent, controller, btn_start, btn_quiz):
        Frame.__init__(self, parent)
        self.selected_index = None
        self.selected_tuple = None
        self.searched_tuple = None

        # Commands
        def get_selected_row(event):
            try:
                self.selected_index = frame4.list1.curselection()[0]
                print(self.selected_index)
                self.selected_tuple = frame4.list1.get(self.selected_index)
                frame2.entry1.delete(0, END)
                frame2.entry1.insert(END, self.selected_tuple[1])
                frame4.text1.delete(1.0, END)
                for line in enumerate(self.selected_tuple[2].split("; "), 1):
                    frame4.text1.insert(END, "{}. {}\n".format(line[0], line[1]))
            except IndexError:
                pass
    
        def search_command():
            try:
                self.searched_tuple = Backend.search(frame2.entry1.get())
            except:
                try:
                    self.searched_tuple = Backend.search(frame2.entry1.get().title())
                except:
                    try:
                        self.searched_tuple = Backend.search(frame2.entry1.get().upper())
                    except:
                        word_options = Backend.word_list(frame2.entry1.get())
                        for word in word_options:
                            result = messagebox.askyesnocancel("No Word Found","Did you mean {} instead?".format(word))
                            if result == True:
                                self.searched_tuple = Backend.search(word)
                                break
                            elif result == False:
                                continue
                            else:
                                break
                            
            frame2.entry1.delete(0, END)
            frame2.entry1.insert(END, self.searched_tuple[1])
            frame4.text1.delete(1.0, END)
            for line in enumerate(self.searched_tuple[2].split("; "), 1):
                frame4.text1.insert(END, "{}. {}\n".format(line[0], line[1]))

        def add_command():
            frame4.list1.delete(0, END)
            try:
                Backend.insert(self.searched_tuple[1], self.searched_tuple[2])
                frame4.list1.insert(END, (self.searched_tuple[1], self.searched_tuple[2]))
            except:
                frame4.list1.insert(END, "The word has been added before.")

        def view_command():
            frame4.list1.delete(0, END)
            for row in Backend.view():
                frame4.list1.insert(END, row)

        def delete_command():
            Backend.delete(self.selected_tuple[0])
            print(self.selected_index)
            frame4.list1.delete(self.selected_index,self.selected_index)

        # CreateFrames
        label = Label(self, text="Dictionary", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        frame1 = Frame(self)
        frame1.pack()

        frame1.button1 = Button(frame1, text="Back to Home Page", width = 25, bg = 'MediumPurple1', 
                            command=lambda: controller.show_frame(btn_start))
        frame1.button1.pack(side = LEFT, padx = 10, pady = 5)

        frame1.button2 = Button(frame1, text="Go to Quiz", width = 25, bg = 'RosyBrown1',
                            command=lambda: controller.show_frame(btn_quiz))
        frame1.button2.pack(side = LEFT, padx = 10, pady = 5)

        frame2 = Frame(self)
        frame2.pack()

        frame2.label1 = Label(frame2, text = 'Enter a Word', width = 15)
        frame2.label1.pack(side = LEFT, padx = 5, pady = 10)
        frame2.entry1 = Entry(frame2, width = 40)
        frame2.entry1.pack(side = LEFT, padx = 5)
        frame2.entry1.focus()
        frame2.button1 = Button(frame2, text = 'Search the Word', width = 15, command = search_command)
        frame2.button1.pack(side = RIGHT, padx = 5, pady = 10)

        frame3 = Frame(self)
        frame3.pack()

        frame3.button1 = Button(frame3, text = 'Marked as Learned', width = 25, bg = 'SpringGreen2', command = add_command)
        frame3.button1.pack(side = LEFT)
        frame3.button2 = Button(frame3, text = 'View All Learned', width = 25, bg = 'LightSkyBlue1', command = view_command)
        frame3.button2.pack(side = LEFT)
        frame3.button3 = Button(frame3, text = 'Delete from Learned', width = 25, bg = 'PaleVioletRed1', command = delete_command)
        frame3.button3.pack(side = LEFT)

        frame4 = Frame(self)
        frame4.pack()

        frame4.list1 = Listbox(frame4, width = 35, height = 30)
        frame4.list1.pack(side = LEFT, pady = 50, padx = 10, fill = Y)
        frame4.sb1 = Scrollbar(frame4)
        frame4.sb1.pack(side = LEFT, fill = Y, pady = 50, )
        frame4.list1.configure(yscrollcommand = frame4.sb1.set)
        frame4.sb1.configure(command = frame4.list1.yview)
        frame4.text1 = Text(frame4, width = 50, height = 30, background = 'white', wrap = WORD)
        frame4.text1.pack(side = LEFT, pady = 50, padx = 10, fill = Y)

        frame4.list1.bind('<<ListboxSelect>>', get_selected_row)












        

