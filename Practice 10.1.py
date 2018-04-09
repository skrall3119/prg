class Person:

    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

person1 = Person("Alex", "1797 Nashville Lane", "20", "8153556261")
person2 = Person("Justin", "1797 Nashville Lane", "17", "8153561722")
person3 = Person("Sean", "1797 Nashville Lane", "13", "8153556261")
print(person1.get_name())
print(person1.get_address())
print(person1.get_age())
print(person1.get_phone() + '\n')

print(person2.get_name())
print(person2.get_address())
print(person2.get_age())
print(person2.get_phone() + '\n')

print(person3.get_name())
print(person3.get_address())
print(person3.get_age())
print(person3.get_phone())
