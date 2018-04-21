import tkinter


class GUI:

    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create StringVar objects for text
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # Create two frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create the label widgets
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)

        # pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # Create the buttons
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # enter main loop
        tkinter.mainloop()

    def show(self):
        self.name_value.set('Alex')
        self.street_value.set('123 Street St.')
        self.csz_value.set('Oregon, IL, 67038')

my_gui = GUI()
