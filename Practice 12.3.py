# Takes the base number n, and multiplies it by itself by the exp value until said value reaches 1.
def power(n, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return n
    else:
        return n * power(n, exp-1)


# Main program
def main():
    print(power(5, 5))

main()
