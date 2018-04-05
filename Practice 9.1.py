# email address and name interactive menu.

import pickle


def add(dic):  # allows the user to add a name and email pair to the list.
    name = input('Enter the name you wish to add: ')
    email = input('Enter the email you wish to associate with this name: ')
    dic[name] = email
    print("'"+name+"' has been added to the list with email: "+email+".")
    print(dictionary)


def remove(dic):  # removes a name and email pair from the list
    name = input('Enter the name of the person you want removed from your emails: ')
    del dic[name]
    print("'"+name+"' has been removed from the list.")
    print(dictionary)


def change(dic):  # allows the user to change either the name or the email address.
    option = input('Do you want to change the name or the email?: ').lower()
    name = input('Enter the name of the person you want to change: ').lower()
    while name not in dic:
        name = input("That name is not in the list, please enter a name in the list. or use the 'add' command at the command screen to add a new email address:")
    if option == 'name':
        print('Changing name:')
        new_name = input('Please enter the new name: ')
        dic[new_name] = dic[name]
        del dic[name]
        print("name has been changed.")
    elif option == 'email':
        print('Changing email')
        new_email = input('Please enter the new email address: ')
        dic[name] = new_email
        print('email has been changed.')
    print(dic)

dictionary = pickle.load(open("save.p", "rb"))  # opens the pickled document with the list of name/email pairs.

# main program 
print("Welcome. Here is your list of contacts:")
print(dictionary)
commands = 'List of commands: ' + '\n' + 'add' + '\n' + 'remove' + '\n' + 'change' + '\n' 'print' + '\n' + 'quit' + '\n'
print(commands)
user = input("Enter a command: ").lower()
while user != 'quit':
    if user == 'add':
        add(dictionary)
        user = input('Enter a command: ')
    elif user == 'remove':
        remove(dictionary)
        user = input('Enter a command: ')
    elif user == 'change':
        change(dictionary)
        user = input('Enter a command: ')
    elif user == 'print':
        print(dictionary)
        user = input('Enter a command: ')
    else:
        print('Command not found!')
        user = input('Enter a command: ')

pickle.dump(dictionary, open("save.p", "wb"))
print("Data has been saved!")
