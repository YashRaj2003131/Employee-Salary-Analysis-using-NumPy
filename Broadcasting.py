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

# Give every employee a 10% salary hike.
new_salary = salary + (salary * 0.10)
print(new_salary)

