# Base class
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for full-time employees
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return f"{self.name} earns ₹{self.monthly_salary} as a full-time employee."

# Subclass for part-time employees
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total = self.hourly_rate * self.hours_worked
        return f"{self.name} earns ₹{total} as a part-time employee."

# Payroll processing function
def process_payroll(employees):
    for emp in employees:
        print(emp.calculate_salary())

# Example usage
employees = [
    FullTimeEmployee("Ravi", 50000),
    PartTimeEmployee("Sneha", 200, 60),
    FullTimeEmployee("Anita", 60000),
    PartTimeEmployee("Ajay", 150, 40)
]

process_payroll(employees)
