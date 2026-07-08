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

# Find the highest salary.
highest_salary = salary.max()
print(highest_salary)

# Find the lowest salary.
lowest_salary = salary.min()
print(lowest_salary)

# Find the average salary.
avg_salary = salary.mean()
print(avg_salary)

# Find the median salary.
median_salary = np.median(salary)
print(median_salary)

# Find the salary standard deviation.
std_salary = np.std(salary)
print(std_salary)

# Find the salary variance.
var_salary = np.var(salary)
print(var_salary)