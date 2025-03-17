"""Assignment 2: Employee Record System
Develop a program that manages employee records using a dictionary. 
Each employee should have an ID as the key and 
a dictionary as the value storing their name, department, and salary.
Expected Output:
- Add a new employee
- Update an employee’s salary
- Display all employee records
"""

class EmployeeRecordSystem():

    def __init__(self):
        self.employees={}
    
    def add_employee(self, emp_id, name,department,salary):
        if emp_id in self.employees:
            print(f" Employee Id {emp_id} already exists!")
        else:
            self.employees[emp_id]={"name": name, "department":department,"salary":salary}
            print(f"Employee {name} added successfully !")
    
    def update_salary(self, emp_id, new_salary):
        if emp_id in self.employees:
            self.employees[emp_id]["salary"] = new_salary
            print(f"Updated salary for Employee ID {emp_id} to {new_salary}.")
        else:
            print(f"Employee ID {emp_id} not found.")

    def display_employees(self):
        if not self.employees:
            print("No employee records available.")
            return
        print("\nEmployee Records:")
        for emp_id, details in self.employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Department: {details['department']}, Salary: {details['salary']}")

# Function-based menu approach
def run_employee_management():
    system = EmployeeRecordSystem()
    
    menu_options = {
        "1": ("Add Employee", lambda: system.add_employee(
            input("Enter Employee ID: "),
            input("Enter Employee Name: "),
            input("Enter Employee Department: "),
            float(input("Enter Employee Salary: "))
        )),
        "2": ("Update Salary", lambda: system.update_salary(
            input("Enter Employee ID to update salary: "),
            float(input("Enter new salary: "))
        )),
        "3": ("Display Employees", system.display_employees),
        "4": ("Exit", exit)
    }
    
    while True:
        print("\nOptions:")
        for key, (desc, _) in menu_options.items():
            print(f"{key}. {desc}")

        choice = input("Enter your choice: ")
        action = menu_options.get(choice)

        if action:
            action[1]()  # Call the associated function
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_employee_management()
    

    


