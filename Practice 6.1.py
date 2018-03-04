def print_names():
    names = open('names.txt', 'r')
    line = names.readline()
    name_count = 0
    while line != '':
        print(line)
        name_count += 1
        line = names.readline()
    print("There are", name_count, "names in the file.")
print_names()
