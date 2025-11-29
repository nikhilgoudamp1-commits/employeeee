import employee

def test_get_employee_details():
    name = "Alice"
    emp_id = "E200"
    department = "Finance"
    salary = 60000

    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E200\n"
        "Department: Finance\n"
        "Salary: 60000"
    )

    result = employee.get_employee_details(name, emp_id, department, salary)
    assert result == expected_output
