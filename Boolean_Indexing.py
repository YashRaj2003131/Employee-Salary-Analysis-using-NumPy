import numpy as np

employee_id = np.arange(101, 111)

age = np.array([23, 28, 35, 41, 26, 30, 45, 38, 29, 32])

salary = np.array([
    350000,
    450000,
    700000,
    1200000,
    400000,
    600000,
    1800000,
    950000,
    550000,
    750000
])

experience = np.array([1, 3, 8, 15, 2, 5, 20, 12, 4, 6])

performance = np.array([3.8, 4.2, 4.5, 4.9, 3.9, 4.3, 5.0, 4.7, 4.1, 4.4])

# Find employees who satisfy both: Salary > ₹600,000 Experience > 5 years
condition1 = (salary > 600000) & (experience > 5)
print(employee_id[condition1])

# Find employees who satisfy: Age < 30 Salary < ₹500,000
condition2 = (age < 30) & (salary < 500000)
print(employee_id[condition2])

# Find employees with: Performance > 4.5 Salary > ₹1,000,000
condition3 = (performance > 4.5) & (salary > 1000000)
print(employee_id[condition3])