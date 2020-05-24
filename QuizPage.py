from tkinter import *
from difflib import get_close_matches
import Backend
import random
import time

LARGE_FONT= ("Verdana", 12)

class QuizPage(Frame):

    def __init__(self, parent, controller, btn_start, btn_dict):
        Frame.__init__(self, parent)
        self.four_word_dict = dict()
        self.button_answer_dict = dict()
        self.correct_answer = 0
        self.selected_database = None
        self.selected_word_or_def = None

        # Create the commands
        def generate_quiz(database, word_or_def):
            selected_word = Backend.generate_random(database)
            word_options = Backend.word_list(selected_word)
            for word in word_options:
                word_tup = Backend.search(word)
                self.four_word_dict[word] = Backend.get_definition(word_tup)
            frame3.text1.delete(1.0, END)
            random.shuffle(word_options)
            button_list = [frame4.button0, frame4.button1, frame4.button2, frame4.button3]
            self.selected_database = database
            self.selected_word_or_def = word_or_def
            if word_or_def == 'word':
                frame3.text1.insert(END, selected_word)
                for button,word in zip(button_list, word_options): 
                    button.config(text = self.four_word_dict[word], wraplength = 350, justify = CENTER, fg = 'black')
                    if word == selected_word:
                        self.button_answer_dict[button] = 1
                    else:
                        self.button_answer_dict[button] = 0
            elif word_or_def == 'definition':
                frame3.text1.insert(END, self.four_word_dict[selected_word])
                for button,word in zip(button_list, word_options): 
                    button.config(text = word, wraplength = 350, justify = CENTER, fg = 'black')
                    if word == selected_word:
                        self.button_answer_dict[button] = 1
                    else:
                        self.button_answer_dict[button] = 0
                else:
                    pass

        def answerClick(button):
            if self.button_answer_dict[button] == 1:
                self.correct_answer += 1
                if self.correct_answer > 0:
                    frame1.label2.config(text = self.correct_answer, fg = 'green')
                else:
                    frame1.label2.config(text = self.correct_answer, fg = 'red')
                generate_quiz(self.selected_database, self.selected_word_or_def)
            else:
                button.config(text = 'Wrong!', fg = 'red')
                self.correct_answer -= 1
                if self.correct_answer > 0:
                    frame1.label2.config(text = self.correct_answer, fg = 'green')
                else:
                    frame1.label2.config(text = self.correct_answer, fg = 'red')
                frame1.label2.config(text = self.correct_answer)

        def clear_count():
            self.correct_answer = 0
            frame1.label2.config(text = self.correct_answer)

        # Create Frames (frontend interface)
        label = Label(self, text="Quiz", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        frame1 = Frame(self)
        frame1.pack()

        frame1.button1 = Button(frame1, text="Back to Home Page", width = 25, bg = 'MediumPurple1', 
                            command=lambda: controller.show_frame(btn_start))
        frame1.button1.pack(side = LEFT, padx = 10, pady = 5)
        frame1.button2 = Button(frame1, text="Go to Dictionary", width = 25, bg = 'RosyBrown1',
                            command=lambda: controller.show_frame(btn_dict))
        frame1.button2.pack(side = LEFT, padx = 10, pady = 5)
        frame1.label1 = Label(frame1, text = 'Points', wid = 15)
        frame1.label1.pack(side = LEFT)
        frame1.label2 = Label(frame1, text = self.correct_answer, bg = 'white')
        frame1.label2.pack(side = LEFT)

        frame2 = Frame(self)
        frame2.pack()

        frame2.button1 = Button(frame2, text = "Random Learned Word", width = 20, bg = 'khaki1', command = lambda: generate_quiz('learned_words', 'word'))
        frame2.button1.pack(side = LEFT, padx = 10, pady = 5)
        frame2.button2 = Button(frame2, text = "Random Learned Definition", width = 20, bg = 'salmon', command = lambda: generate_quiz('learned_words', 'definition'))
        frame2.button2.pack(side = LEFT, padx = 10, pady = 5)
        frame2.button3 = Button(frame2, text = "Random All Word", width = 20, bg = 'turquoise', command = lambda: generate_quiz('dictionary', 'word'))
        frame2.button3.pack(side = LEFT, padx = 10, pady = 5)
        frame2.button4 = Button(frame2, text = "Random All Definition", width = 20, bg = 'thistle2', command = lambda: generate_quiz('dictionary', 'definition'))
        frame2.button4.pack(side = LEFT, padx = 10, pady = 5)
        frame2.button4 = Button(frame2, text = "Clear Counter", width = 20, bg = 'SlateBlue1', command = clear_count)
        frame2.button4.pack(side = LEFT, padx = 10, pady = 5)

        frame3 = Frame(self)
        frame3.pack()

        frame3.text1 = Text(frame3, bg = 'white', width = 60, height = 5, wrap = WORD)
        frame3.text1.pack(side = LEFT, padx = 10, pady = 5)

        frame4 = Frame(self)
        frame4.pack()

        frame4.button0 = Button(frame4, text = '', width = 50, height = 4, command = lambda: answerClick(frame4.button0))
        frame4.button0.pack(side =TOP)

        frame4.button1 = Button(frame4, text = '', width = 50, height = 4, command = lambda: answerClick(frame4.button1))
        frame4.button1.pack(side =TOP)

        frame4.button2 = Button(frame4, text = '', width = 50, height = 4, command = lambda: answerClick(frame4.button2))
        frame4.button2.pack(side =TOP)

        frame4.button3 = Button(frame4, text = '', width = 50, height = 4, command = lambda: answerClick(frame4.button3))
        frame4.button3.pack(side =TOP)
