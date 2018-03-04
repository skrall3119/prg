def average(lst):  # find average of list and return it
    ave = 0  # variable to store average
    for count in range(len(lst)):
        ave += lst[count]
    ave /= len(lst)
    return ave


def total_rainfall(lst):  # find total rain fall of list and return it trf=total rain fall
    trf = 0  # variable to store total
    for count in range(len(lst)):
        trf += lst[count]
    return trf


def highest(items):  # highest number of rain fall of list and return it
    high = 0  # variable to store highest
    for j in range(len(items)):
        if items[j] > high:
            high = items[j]
    return highest


def lowest(items):  # lowest number of rain fall of list and return it
    low = items[1]  # variable to store lowest
    for k in range(len(items)):
        if items[k] < low:
            low = items[k]
    return lowest

rainfall = []  # stores each months rainfall amount

for i in range(12):
    rainfall.append(int(input("How much rainfall for month %d?" % (i+1))))

print("the total rain fall is", total_rainfall(rainfall))
print("the average rain fall is", average(rainfall))
print("the highest number of  rain fall is", highest(rainfall))
print("the lowest number of rain fall is", lowest(rainfall))
