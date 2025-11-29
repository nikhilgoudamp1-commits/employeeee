import sys

def get_employee_details(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

if __name__ == "__main__":
    try:
        if len(sys.argv) == 5:
            name, emp_id, department = sys.argv[1:4]
            salary = float(sys.argv[4])
        else:
            name, emp_id, department, salary = "John Doe", "E101", "HR", 55000

        print("\n=== Employee Details ===")
        print(get_employee_details(name, emp_id, department, salary))

    except ValueError:
        print("Error: Salary must be a number.")
