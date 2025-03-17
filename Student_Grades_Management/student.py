"""Assignment 1: Student Grades Management
Create a Python program that stores student names and their grades using a list of tuples. 
The program should allow adding new students, updating grades, and displaying all students with their grades.
Expected Output:
- Add a student with a grade
- Update an existing student’s grade
- Display all students with their grades"""

class StudentGrades:

    def __init__(self):
        self.students=[]

    def add_student(self, name:str,grade:str):
        self.students.append((name,grade))
        print(f"Student name {name} with grade {grade} is sucessfully added!")

    def update_grade(self,name:str, new_grade:str):
        for i , (student_name, new_grade) in enumerate (self.students):
            if student_name==name:
                self.students[i]=(name,new_grade)
                print(f"Student {name}'s updated grade to {new_grade} ")
                return
        print(f"Student {name} not found!")

    def display_students(self):
        if not self.students:
            print ("No Student Available")
            return
        print("\n Student's Grades: ")
        for name, grade in self.students:
            print(f"Student Name : {name} - Grade : {grade}")

def main():
    manager = StudentGrades()

    while True :
        print("\nOptions:")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Display Students")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            manager.add_student(name, grade)
        elif choice == "2":
            name = input("Enter student name to update: ")
            new_grade = input("Enter new grade: ")
            manager.update_grade(name, new_grade)
        elif choice == "3":
            manager.display_students()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




