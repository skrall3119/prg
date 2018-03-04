def read_boys():
    file = open('BoyNames.txt', 'r')
    line = file.readline()
    boy_list = []
    while line != '':
        boy_list.append(line.strip('\n'))
        line = file.readline()
    return boy_list


def read_girls():
    file = open('GirlNames.txt', 'r')
    line = file.readline()
    girl_list = []
    while line != '':
        girl_list.append(line.strip('\n'))
        line = file.readline()
    return girl_list


def get_input():
    line = input("Please enter a boy name or girls name: ")
    return str(line)


boys = read_boys()
girls = read_girls()
user = get_input()

if user in boys or user in girls:
	print("Popular name!")
else:
	print("Not in the list!")