from tkinter import *
from functools import partial


class Business:

    def __init__(self, master):
        # Creates the main frame
        frame = Frame(master)

        # Initializes the main variables and data structures for the program.
        self.total = 0.0
        self.label_text = StringVar()
        self.label_text.set('Your total today will be: $0.00')
        self.prices = [6.29, 4.59, 1.07, 1.07, 1.3, 1.07, .99, 3.29, 3.99, 10.99]
        self.colors = ["#f6e83e", "#fffa9e", "#4d1b00", "#ff630f", "red", "blue", "magenta", '#491e0e', '#38b382', '#6b8964']
        self.products = ['Cheesecake', 'Ice Cream', "Hershey's", "Reese's", "Take-5", "Snickers", "Bubble Gum", 'Cookies', "Brownies", "Cake"]

        # Creates the buttons and colorful labels. It creates a label for each of the 10 products, each with a corresponding color,
        # then creates a button with the corresponding price as the text parameter. The partial command allows for the total to be updated, otherwise it simply wouldn't work.
        r = 0
        for p in self.products:
            Label(frame, text=p, bg=self.colors[r]).grid(row=r, column=0)
            Button(frame, text="${:0,.2f}".format(self.prices[r]), command=partial(self.update_total, self.prices[r])).grid(row=r, column=1)
            r += 1

        # label that updates as buttons are pressed.
        self.total_label = Label(frame, textvariable=self.label_text).grid(row=11, column=0)

        frame.pack()

    # changes the textvariable in total_label after each click.
    def update_total(self, value):
        self.total += value
        self.label_text.set("Your total today will be: " + "${:0,.2f}".format(self.total))

root = Tk()
Business(root)
root.mainloop()
