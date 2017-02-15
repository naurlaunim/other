from tkinter import *
import random

class ToDoList:
    def __init__(self, *args):
        self.urgent = list(args)
        self.long_term = []
        self.root = Tk()
        self.current = StringVar()
        self.str = StringVar()
        self.start()
        self.make_widgets()
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
        if self.urgent != []:
            i = random.choice(range(len(self.urgent)))
            self.current.set(self.urgent[i])
            del self.urgent[i]
        else:
            self.current.set('')

    def done(self):
        if self.urgent != []:
            i = random.choice(range(len(self.urgent)))
            self.current.set(self.urgent[i])
            del self.urgent[i] ##
            self.task_message.configure(fg = 'red')
        elif self.long_term != []:
            i = random.choice(range(len(self.long_term)))
            self.current.set(self.long_term[i])
            del self.long_term[i]
            self.task_message.configure(fg = 'blue')
        else:
            self.current.set('')

    def add_long_term(self):
        if self.str != '':
            self.long_term.append(self.str.get())
            self.str.set('')

    def add_urgent(self):
        if self.str != '':
            self.urgent.append(self.str.get())
            self.str.set('')



if __name__ == '__main__':
    root = ToDoList()

