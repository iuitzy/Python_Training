from .Employee import Employee

class FreeLancer(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked

    def calculate_salary(self):
        salary=self.hourly_rate*self.hours_worked
        self.set_salary(salary)
        return f"{self.name}'s Freelancer Payment: ${self.get_salary()} "
    