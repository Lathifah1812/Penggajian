class Employee:
    def __init__(self, name: str, salary: int, grade: int, num_children: int, married: bool):
        self.name = name
        self.salary = salary
        self.grade = grade
        self.num_children = num_children
        self.married = married
    
    def get_grade_allowance(self, grade: int) -> float:
        if grade == 1:
            allowance_grade = 0.05 * self.salary
        elif grade == 2:
            allowance_grade = 0.1 * self.salary
        elif grade == 3:
            allowance_grade = 0.15 * self.salary
        elif grade == 4:
            allowance_grade = 0.2 * self.salary
        else:
            allowance_grade = 0
        return allowance_grade
    
    def get_children_allowance(self, num_children: int) -> float:
        if num_children > 0:
            allowance_children = 0.02 * self.salary * num_children
        else:
            allowance_children = 0
        return allowance_children
    
    def get_spouse_allowance(self, married: bool) -> float:
        if married:
            allowance_spouse = 0.1 * self.salary
        else:
            allowance_spouse = 0
        return allowance_spouse
    
    def get_salary(self) -> float:
        total_salary = self.salary + self.get_grade_allowance(self.grade) + self.get_children_allowance(self.num_children) + self.get_spouse_allowance(self.married)
        
        if total_salary <= 5000000:
            tax = 0.05 * total_salary
        elif total_salary <= 10000000:
            tax = 0.1 * total_salary
        else:
            tax = 0.15 * total_salary

        if self.grade == 3 and self.num_children >= 3:
            bonus = 500000
        elif self.grade == 4 and self.num_children >= 4:
            bonus = 1000000
        else:
            bonus = 0
            
        total_salary = total_salary - tax + bonus
        return total_salary

name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))
grade = int(input("Enter employee grade (1-4): "))
num_children = int(input("Enter number of employee's children: "))
married = input("Is employee married (yes/no): ").lower() == "yes"

emp = Employee(name, salary, grade, num_children, married)
salary = emp.get_salary()

print(f"{emp.name} has a salary of {salary}")
