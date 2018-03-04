def find_average(value_list):  # finds the average based on the file
    total = 0
    k = 0
    while value_list[k] <= len(value_list) - 1:
        total += value_list[k]
        k += 1
    average = total / len(value_list)
    print(average)


def get_numbers():
    file = open('numbers.txt', 'r')
    line = file.readline()
    numbers = []
    while line != '':
        numbers.extend(line.strip().split('\n'))
        line = file.readline()
    numbers = [int(i) for i in numbers]
    return numbers
current_list = get_numbers()
find_average(current_list)
