import numpy as np

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

salary[6] = 10000000

# Find the mean salary.
mean_salary = np.mean(salary)
print(mean_salary)

# Find the median salary.
median = np.median(salary)
print(median)

#---------------------   Explanation   ---------------------
# After changing one salary to ₹10,000,000:
# Mean salary: ₹1,595,000
# Median salary: ₹650,000
# 
# The mean is calculated by adding all salaries and dividing by the number of employees.
# When one employee's salary increases from ₹1,800,000 to ₹10,000,000, the total salary increases by
# ₹8,200,000. This large increase raises the average for everyone.
# 
# Mean is sensitive to outliers because every value contributes to the calculation.
# Median is resistant to outliers because it only depends on the middle position of the sorted data.

