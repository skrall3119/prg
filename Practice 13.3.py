from tkinter import *
from tkinter import messagebox


class MilesPerGallon:

    def __init__(self, master):
        frame = Frame(master)
        button_frame = Frame(master)

        self.label_1 = Label(frame, text='Tank size in gallons:', bg='red', fg='white')
        self.label_2 = Label(frame, text='miles that can be driven on a full tank', bg='blue', fg='white')

        self.entry_1 = Entry(frame)
        self.entry_2 = Entry(frame)

        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.printButton = Button(button_frame, text="Convert!", command=self.convert, bg='blue', fg='white')
        self.printButton.pack(side=LEFT)

        self.quit_button = Button(button_frame, text='Quit', command=frame.quit)
        self.quit_button.pack(side=LEFT)

        self.label_1.grid(row=0, column=0)
        self.label_2.grid(row=1, column=0)

        frame.pack(side=LEFT)
        button_frame.pack(side=RIGHT)

    def convert(self):
        mpg = int(self.entry_2.get()) / int(self.entry_1.get())
        messagebox.showinfo("Your car can drive", str(mpg) + " miles per gallon")

root = Tk()
MilesPerGallon(root)
root.mainloop()
