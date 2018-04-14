import Furniture


def main():

    desk = Furniture.Furniture("desk", "wood", 3, 2.5, 3.2, 400)
    drawers = Furniture.Desk("desk", "wood", 3, 2.5, 3.2, 400, 3, "left")

    print(desk)
    print(drawers)


main()
