from tkinter import *
from tkinter import messagebox
import pickle
import collections
from functools import partial


# Root Window
class CrudMain:

    # Creates all buttons, labels, the button frame, sets the title text, in the root window.
    def __init__(self, master, cust):
        self.master = master
        self.customer_list = cust

        self.cust_frame = Frame(self.master)
        self.button_list = {}
        frame = Frame(self.master)
        frame.master.title("Contact List Editor")

        self.label_1 = Label(frame, text='Contact list').pack(side=LEFT)

        self.update_customers()

        self.add_button = Button(frame, text='Add Contact', command=self.add_contact_window)
        self.update_button = Button(frame, text='Refresh', command=lambda: self.update_customers())
        self.clear_button = Button(frame, text='Clear Contacts', command=lambda: self.clear_list())

        self.add_button.pack(anchor='e')
        self.update_button.pack(anchor='e')
        self.clear_button.pack(anchor='e')
        frame.pack(anchor='nw')
        self.cust_frame.pack(anchor='w')

    # opens the "add contact" window
    def add_contact_window(self):
        AddWindow(self.master, self, self.customer_list)
        self.cust_frame.update()

    # This function "refreshes" the root window by deleting all the contact buttons, and then replaces them, adding new ones if necessary.
    def update_customers(self):
        for widget in self.cust_frame.winfo_children():
            widget.destroy()

        r = 0
        for key in self.customer_list:
            Button(self.cust_frame, text=key, command=partial(self.cust_info, key)) .grid(row=1, column=r)
            r += 1

    # Opens the customer information window.
    def cust_info(self, key):
        CustInfo(self.master, self.customer_list, self, key, self.button_list)

    # Allows the user to totally wipe the entire contact list.
    def clear_list(self):
        for button in self.button_list:
            self.button_list[button].destroy()
        self.customer_list.clear()
        pickle.dump(self.customer_list, open('customer_file.dat', 'wb'))
        messagebox.showinfo("Status", "Information has been wiped!")


# Customer information class.
class CustInfo:

    # initializes all buttons, labels and variables in the Customer Information window. from here the user can either edit or delete the information, as well as close the window.
    def __init__(self, master, cust, main_window, key, button_list):
        self.master = master
        self.cust_list = cust
        self.main_window = main_window
        self.key = key
        self.button_list = button_list

        self.cust = cust[key]
        self.info_window = Toplevel()
        self.info_window.title("Contact Information")

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phone = StringVar()

        self.first_name.set(self.cust['first_name'])
        self.last_name.set(self.cust['last_name'])
        self.email.set(self.cust['email'])
        self.address.set(self.cust['address'])
        self.phone.set(self.cust['phone'])

        self.first_label = Label(self.info_window, textvariable=self.first_name).pack()
        self.last_label = Label(self.info_window, textvariable=self.last_name).pack()
        self.email_label = Label(self.info_window, textvariable=self.email).pack()
        self.address_label = Label(self.info_window, textvariable=self.address).pack()
        self.phone_label = Label(self.info_window, textvariable=self.phone).pack()

        Button(self.info_window, text='Close', command=self.info_window.destroy).pack(side=LEFT)
        Button(self.info_window, text='Edit', command=self.edit_info).pack(side=LEFT)
        Button(self.info_window, text='Delete', command=lambda: self.delete_cust(self.cust_list, key)).pack(side=LEFT)
        Button(self.info_window, text='Refresh', command=lambda: self.update_info()).pack(side=LEFT)

    # deletes the information that is being viewed.
    def delete_cust(self, cust, key):
        del cust[key]
        messagebox.showinfo("Item delete", "User has been deleted!")
        pickle.dump(cust, open('customer_file.dat', 'wb'))
        self.main_window.update_customers()
        self.info_window.destroy()

    # opens the editor to allow changes to be made to the current person.
    def edit_info(self):
        EditWindow(self.master, self.cust, self, self.cust_list, self.key)

    # makes sure the displayed information is what is stored on the file.
    def update_info(self):

        self.first_name.set(self.cust_list[self.key]['first_name'])
        self.last_name.set(self.cust_list[self.key]['last_name'])
        self.email.set(self.cust_list[self.key]['email'])
        self.address.set(self.cust_list[self.key]['address'])
        self.phone.set(self.cust_list[self.key]['phone'])


# The information editor window. Creates two buttons and five entry widgets with the data that was stored on the file.
#  Changing the first name of a person Creates a new person in the dictionary that takes the rest of the data with it.
class EditWindow:

    def __init__(self, master, cust, cust_window, cust_list, key):
        self.master = master
        self.cust = cust
        self.cust_list = cust_list
        self.cust_window = cust_window
        self.key = key
        self.edit_window = Toplevel()

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phone = StringVar()

        self.first_name.set(self.cust['first_name'])
        self.last_name.set(self.cust['last_name'])
        self.email.set(self.cust['email'])
        self.address.set(self.cust['address'])
        self.phone.set(self.cust['phone'])

        Label(self.edit_window, text='First Name: ').grid(row=0, column=0)
        Label(self.edit_window, text='Last Name: ').grid(row=1, column=0)
        Label(self.edit_window, text='Email Address: ').grid(row=2, column=0)
        Label(self.edit_window, text='Street Address: ').grid(row=3, column=0)
        Label(self.edit_window, text='Phone Number:').grid(row=4, column=0)

        Button(self.edit_window, text="Submit", command=partial(self.save)).grid(row=5, column=0)
        Button(self.edit_window, text='Cancel', command=self.edit_window.destroy).grid(row=5, column=1)

        Entry(self.edit_window, textvariable=self.first_name).grid(row=0, column=1)
        Entry(self.edit_window, textvariable=self.last_name).grid(row=1, column=1)
        Entry(self.edit_window, textvariable=self.email).grid(row=2, column=1)
        Entry(self.edit_window, textvariable=self.address).grid(row=3, column=1)
        Entry(self.edit_window, textvariable=self.phone).grid(row=4, column=1)

    # takes the information entered in the entry widgets, stores it in a nested dictionary, and then writes it to a file.
    def save(self):

        name = str(self.first_name.get())
        last = str(self.last_name.get())
        email = str(self.email.get())
        address = str(self.address.get())
        phone = str(self.phone.get())

        save = {'first_name': name, 'last_name': last, 'email': email, 'address': address, 'phone': phone}
        del self.cust
        new_key = save['first_name']
        self.cust_list[new_key] = save

        pickle.dump(self.cust_list, open('customer_file.dat', 'wb'))
        messagebox.showinfo("Status", "Information saved successfully!")
        self.edit_window.destroy()
        self.cust_window.update_info()


# Creates the Add Window. Allows user to enter a new person, and a button is created on the root window.
class AddWindow:

    def __init__(self, master, main_window, cust):
        self.master = master
        self.cust = cust
        self.main_window = main_window

        self.add_window = Toplevel()
        self.add_window.title("Add Contact")

        Label(self.add_window, text='First Name: ').grid(row=0, column=0)
        Label(self.add_window, text='Last Name: ').grid(row=1, column=0)
        Label(self.add_window, text='Email Address: ').grid(row=2, column=0)
        Label(self.add_window, text='Street Address: ').grid(row=3, column=0)
        Label(self.add_window, text='Phone Number:').grid(row=4, column=0)

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phone = StringVar()

        Button(self.add_window, text="Submit", command=lambda: self.save_new(self.cust)).grid(row=5, column=0)
        Button(self.add_window, text='Cancel', command=self.add_window.destroy).grid(row=5, column=1)

        Entry(self.add_window, textvariable=self.first_name).grid(row=0, column=1)
        Entry(self.add_window, textvariable=self.last_name).grid(row=1, column=1)
        Entry(self.add_window, textvariable=self.email).grid(row=2, column=1)
        Entry(self.add_window, textvariable=self.address).grid(row=3, column=1)
        Entry(self.add_window, textvariable=self.phone).grid(row=4, column=1)

    # almost the same function from the edit window, except all information is first stored in a dictionary.
    # the value at 'first_name' becomes the key to this dictionary in another dictionary, for all the other contacts entered.
    def save_new(self, customers):
        name = str(self.first_name.get())
        last = str(self.last_name.get())
        email = str(self.email.get())
        address = str(self.address.get())
        phone = str(self.phone.get())

        save = {'first_name': name, 'last_name': last, 'email': email, 'address': address, 'phone': phone}
        key = save['first_name']
        customers[key] = save
        pickle.dump(customers, open('customer_file.dat', 'wb'))
        messagebox.showinfo("Status", "Information saved successfully!")
        self.add_window.destroy()
        self.main_window.update_customers()

# main loop of the program. Checks to see if a file exists, if not, creates a new empty dictionary.
def main():
    try:
        input_file = open("customer_file.dat", "rb")
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        customers = collections.OrderedDict()

    root = Tk()
    CrudMain(root, customers)
    root.mainloop()

main()
