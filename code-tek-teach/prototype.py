
import copy

class Employee:
    def __init__(self,name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} lives at {self.address}'


class Address:
    def __init__(self, city_name, street,suite):
        self.suite = suite
        self.city_name = city_name
        self.street = street

    def __str__(self):
        return f'{self.city_name}:{self.street} '



class EmployeeFactory:
    main_office_employee = Employee('', Address('123 london', 0, 'London'))
    aux_office_employee = Employee('', Address('123B', 0, 'London'))


    @staticmethod
    def __new_employee(proto,name,suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return suite
    
    @staticmethod
    def new_main_office_employee(name,suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )
    
john = EmployeeFactory.new_main_office_employee('john',101)
jane = EmployeeFactory.new_aux_main_office_employee('jane',122)

print(jane)
print(john)