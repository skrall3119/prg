def find_sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + find_sum(list[1:])


def main():
    list = [2, 7, 43, 15, 76, 22]
    print(find_sum(list))

main()
