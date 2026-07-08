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

# Find the shape of each array.

print(employee_id.shape)
print(age.shape)
print(salary.shape)
print(experience.shape)
print(performance.shape)

# Find the data type of each array.

print(employee_id.dtype)
print(age.dtype)
print(salary.dtype)
print(experience.dtype)
print(performance.dtype)

# Find the number of dimensions.

print(employee_id.ndim)
print(age.ndim)
print(salary.ndim)
print(experience.ndim)
print(performance.ndim)

# Find the total number of employees.

total_employees = employee_id.size
print(total_employees)