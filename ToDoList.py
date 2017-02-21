#!/usr/bin/env python3
from tkinter import *
import random
import pickle

class ToDoList:
    def __init__(self, *args):
        self.urgent = list(args)
        self.long_term = []
        self.root = Tk()
        self.current = StringVar()
        self.str = StringVar() # Entry textvariable
        self.make_widgets()
        self.start()
        self.root.mainloop()


    def make_widgets(self):
        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        self.left_frame.grid(row = 0, column = 0, padx = 6, pady = 3)
        self.right_frame.grid(row = 0, column = 1, padx = 6, pady = 3)

        self.task_message = Message(self.left_frame, textvariable = self.current, fg = 'red', width = 200)
        self.done_button = Button(self.left_frame, text = 'сделано.', command = self.done)
        self.task_message.grid(row = 0, column = 0, pady = 0)
        self.done_button.grid(row = 1, column = 0)

        self.entry = Entry(self.right_frame, textvariable = self.str)
        self.add_button = Button(self.right_frame, text = 'добавить', command = self.add_long_term)
        self.add_urgent_button = Button(self.right_frame, text = 'в срочные', command = self.add_urgent)
        self.entry.grid(row = 0, column = 0, columnspan = 2, pady = 2)
        self.add_button.grid(row = 1, column = 0)
        self.add_urgent_button.grid(row = 1, column = 1)

        self.root.title('to-do list')

    def start(self):
        try:
            f1 = open('urgent_list.txt', 'rb')
            self.urgent += pickle.load(f1)
        except FileNotFoundError:
            pass
        try:
            f2 = open('long_time_list.txt', 'rb')
            self.long_term = pickle.load(f2)
        except FileNotFoundError:
            pass
        try:
            f3 = open('current.txt', 'rb')
            self.current.set(pickle.load(f3)) ##
        except FileNotFoundError:
            self.current.set('')

        if not self.current.get():
            self.done()

    def done(self):
        if self.urgent:
            self.set_new(self.urgent, 'urgent_list.txt')
            self.task_message.configure(fg = 'red')
        elif self.long_term:
            self.set_new(self.long_term, 'long_time_list.txt')
            self.task_message.configure(fg = 'blue')
        else:
            self.current.set('')
        self.save(self.current.get(), 'current.txt')

    def set_new(self, _list, _list_name):
        i = random.choice(range(len(_list)))
        self.current.set(_list[i])
        del _list[i]
        self.save(_list, _list_name)

    def add_long_term(self):
        self.add_to_list(self.long_term)
        self.save(self.long_term, 'long_time_list.txt')

    def add_urgent(self):
        self.add_to_list(self.urgent)
        self.save(self.urgent, 'urgent_list.txt')

    def add_to_list(self, _list):
        if self.str.get():
            _list.append(self.str.get())
            self.str.set('')

    def save(self, _list, _list_name):
        f = open(_list_name, 'wb')
        pickle.dump(_list, f)
        f.close()


if __name__ == '__main__':
    root = ToDoList()

