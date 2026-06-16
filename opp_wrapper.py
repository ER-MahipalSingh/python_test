class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name} age: {self.age}")
        
class Employee(Person):
    def __int__(self, name, age, employee_id=None, salary=0.0):
        super().__int__(name, age)
        self.__employee_id = employee_id
        self.__salary = float(salary)
        
def __del__(self):
    pass

def get_employee_id(self):
    return self.__employee_id

def set_employee_id(self, emp_id):
    self.__employee_id = emp_id
    
def set_salary(self, salary):
    if salary >= 0:
        self.__salary = float(salary)
    else:
        print("Salary cannot be negative")
        
def display(self):
    print("\nEmployee Details: ")
    super.display()
    print(f"Employee ID: {self.__employee_id}")
    print(f"Salary: ${self.__salary}")
    
def __str__(self):
    return f"Employee {self.name} ({self.__employee_id})"

def __eq__(self, other):
    return self.get_salary() == other.get_salary()

def __lt__(self, other):
    return self.get_salary() < other.get_salary()

def __gt__(self, other):
    return self.get_salary() > other.get_salary()

class Manager(Employee):
    """Derived class demonstrating inheritance and overriding."""
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")
        
    def __str__(self):
        return f"Manager {self.name} ({self.get_employee_id()})"


class Developer(Employee):
    """Derived class demonstrating inheritance and overriding."""
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
        
    def __str__(self):
        return f"Developer {self.name} ({self.get_employee_id()})"



def main():
    employees_db = {} 
    print("Python OOP Project: Employee Management System")

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Compare Salaries")
        print("6. Verify Class Subclass (issubclass)")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            p = Person(name, age)
            print(f"Person created with name: {name} and age: {age}.")
            
        elif choice == '2':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            
            emp = Employee(name, age, emp_id, salary)
            employees_db[emp_id] = emp
            print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")
            
        elif choice == '3':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            
            mgr = Manager(name, age, emp_id, salary, dept)
            employees_db[emp_id] = mgr
            print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")
            
        elif choice == '4':
            search_id = input("Enter Employee ID to view details: ")
            if search_id in employees_db:
                employees_db[search_id].display()
            else:
                print("Employee not found.")
                
        elif choice == '5':
            print("Choose two employees to compare salaries.")
            id1 = input("Enter the first employee's ID: ")
            id2 = input("Enter the second employee's ID: ")
            
            if id1 in employees_db and id2 in employees_db:
                emp1 = employees_db[id1]
                emp2 = employees_db[id2]
                
                print("\nComparing salaries:")
                if emp1 < emp2:
                    print(f"{emp1} has a lower salary than {emp2}.")
                elif emp1 > emp2:
                    print(f"{emp1} has a higher salary than {emp2}.")
                else:
                    print(f"{emp1} has the exact same salary as {emp2}.")
            else:
                print("One or both Employee IDs not found.")
                
        elif choice == '6':
            print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")
            print(f"Is Developer a subclass of Employee? {issubclass(Developer, Employee)}")
            print(f"Is Employee a subclass of Person? {issubclass(Employee, Person)}")
            
        elif choice == '7':
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break
            
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()