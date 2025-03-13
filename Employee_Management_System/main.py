from .fulltime_employee import FullTimeEmployee
from .freelancer import FreeLancer 
from .salary_processor import process_salary

emp1= FullTimeEmployee("Alice",101,5000)
emp2= FreeLancer("Bob",102,50,160)

process_salary(emp1)
process_salary(emp2)