# Employee Management System 

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name= name
        self.emp_id = emp_id
        self.__salary = 0

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,amount):
        if amount >0:
            self.__salary = amount 
        else:
            print ("Invalid Salary Amount!")



