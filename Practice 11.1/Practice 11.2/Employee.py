# Superclass Employee


class Employee:

    # Constructor method
    def __init__(self, name, emp_number):
        self.__name = name
        self.__emp_number = emp_number

    # mutator methods
    def set_name(self, name):
        self.__name = name

    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_emp_number(self):
        return self.__emp_number

    def __str__(self):
        line = "This is " + self.__name + " with phone number " + self.__emp_number
        return line


# Subclass ProductionWorker
class ProductionWorker(Employee):

    # Constructor method
    def __init__(self, name, emp_number, shift, pay_rate):

        Employee.__init__(self, name, emp_number)

        self.__shift = shift
        self.__pay_rate = pay_rate

    # Mutator methods
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # Accessor methods
    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate
