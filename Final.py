from tkinter import *
from tkinter import messagebox
import pickle
import collections
from functools import partial


class CrudMain:

    def __init__(self, master, cust):
        self.master = master
        self.customer_list = cust

        self.cust_frame = Frame(self.master)
        self.button_list = {}
        frame = Frame(self.master)
        frame.master.title("Contact List Editor")

        self.label_1 = Label(frame, text='Contact list').pack(side=LEFT)
        r = 0

        for key in cust:
            self.cust_frame.grid_forget()
            self.button_list[key] = Button(self.cust_frame, text=key, command=partial(self.cust_info, key, r))
            self.button_list[key].grid(row=1, column=r)
            r += 1

        self.add_button = Button(frame, text='Add Contact', command=self.add_contact_window)
        self.update_button = Button(frame, text='Refresh', command=lambda: self.update(self.customer_list))
        self.clear_button = Button(frame, text='Clear Contacts', command=lambda: self.clear_list())

        self.add_button.pack(anchor='e')
        self.update_button.pack(anchor='e')
        self.clear_button.pack(anchor='e')
        frame.pack(anchor='nw')
        self.cust_frame.pack(anchor='w')

    def update(self, cust):
        r = 0
        for key in cust:
            self.cust_frame.grid_forget()
            self.button_list[key] = Button(self.cust_frame, text=key, command=partial(self.cust_info, key, r))
            self.button_list[key].grid(row=1, column=r)
            r += 1

    def add_contact_window(self):
        AddWindow(self.master, self.customer_list)
        self.cust_frame.update()

    def cust_info(self, key, position):
        CustInfo(self.master, self.customer_list, key, position, self.button_list)

    def clear_list(self):
        for button in self.button_list:
            self.button_list[button].destroy()
        self.customer_list.clear()
        pickle.dump(self.customer_list, open('customer_file.dat', 'wb'))
        messagebox.showinfo("Status", "Information saved successfully!")


class CustInfo:

    def __init__(self, master, cust, key, position, button_list):

        self.button_list = button_list
        self.position = position
        self.master = master
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
        Button(self.info_window, text='Delete', command=lambda: self.delete_cust(cust, key)).pack(side=LEFT)
        Button(self.info_window, text='Refresh', command=lambda: self.update_info()).pack(side=LEFT)

    def delete_cust(self, cust, key):
        del cust[key]
        self.button_list[key].destroy()
        messagebox.showinfo("Item delete", "User has been deleted!")
        pickle.dump(cust, open('customer_file.dat', 'wb'))
        self.info_window.destroy()

    def edit_info(self):
        EditWindow(self.master, self.cust)

    def update_info(self):

        print(self.cust)

        self.first_name.set(self.cust['first_name'])
        self.last_name.set(self.cust['last_name'])
        self.email.set(self.cust['email'])
        self.address.set(self.cust['address'])
        self.phone.set(self.cust['phone'])


class EditWindow:

    def __init__(self, master, cust):
        self.master = master
        self.cust = cust
        self.edit_window = Toplevel()

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phone = StringVar()

        Label(self.edit_window, text='First Name: ').grid(row=0, column=0)
        Label(self.edit_window, text='Last Name: ').grid(row=1, column=0)
        Label(self.edit_window, text='Email Address: ').grid(row=2, column=0)
        Label(self.edit_window, text='Street Address: ').grid(row=3, column=0)
        Label(self.edit_window, text='Phone Number:').grid(row=4, column=0)

        Button(self.edit_window, text="Submit", command=lambda: self.save(self.cust)).grid(row=5, column=0)
        Button(self.edit_window, text='Cancel', command=self.edit_window.destroy).grid(row=5, column=1)

        Entry(self.edit_window, textvariable=self.first_name).grid(row=0, column=1)
        Entry(self.edit_window, textvariable=self.last_name).grid(row=1, column=1)
        Entry(self.edit_window, textvariable=self.email).grid(row=2, column=1)
        Entry(self.edit_window, textvariable=self.address).grid(row=3, column=1)
        Entry(self.edit_window, textvariable=self.phone).grid(row=4, column=1)

    def save(self, customers):

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
        self.edit_window.destroy()


class AddWindow:

    def __init__(self, master, cust):
        self.master = master
        self.cust = cust

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

        Button(self.add_window, text="Submit", command=lambda: self.save(self.cust)).grid(row=5, column=0)
        Button(self.add_window, text='Cancel', command=self.add_window.destroy).grid(row=5, column=1)

        Entry(self.add_window, textvariable=self.first_name).grid(row=0, column=1)
        Entry(self.add_window, textvariable=self.last_name).grid(row=1, column=1)
        Entry(self.add_window, textvariable=self.email).grid(row=2, column=1)
        Entry(self.add_window, textvariable=self.address).grid(row=3, column=1)
        Entry(self.add_window, textvariable=self.phone).grid(row=4, column=1)

    def save(self, customers):
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
