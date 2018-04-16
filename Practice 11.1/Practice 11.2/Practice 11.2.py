import Employee


# Main program
def main():

    # Class variables
    name = input("Please enter the employee name: ")
    number = input("Please enter the employee's phone number: ")
    shift = input("Please enter the shift for this employee: ")
    pay_rate = input("Please enter the pay rate for the employee: ")

    # Class object
    production_worker = Employee.ProductionWorker(name, number, shift, pay_rate)

    # Prints attributes to screen.
    print("Employee Name: " + production_worker.get_name())
    print("Employee phone number: " + str(production_worker.get_emp_number()))
    print("Employee shift: " + str(production_worker.get_shift()))
    print("Employee pay rate ${:0,.2f}".format(int(production_worker.get_pay_rate())))

main()
