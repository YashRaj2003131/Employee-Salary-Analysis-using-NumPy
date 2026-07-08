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

# Find employees earning more than ₹700,000.
earning_more = salary > 700000
print(employee_id[earning_more])

# Find employees earning more than ₹700,000.
earning_less = salary < 500000
print(employee_id[earning_less])

# Find employees older than 30.
older_than = age > 30
print(employee_id[older_than])

# Find employees with more than 10 years of experience.
more_experiance = experience > 10
print(employee_id[more_experiance])

# Find employees with a performance rating above 4.5.
performance_above = performance > 4.5
print(employee_id[performance_above])