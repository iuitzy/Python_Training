from .Employee import Employee 

class FullTimeEmployee(Employee):
    def __init__(self,name,emp_id,monthly_salary):
        super().__init__(name,emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        self.set_salary(self.monthly_salary)
        return f"{self.name}'s Monthly Salary: ${self.get_salary()}"