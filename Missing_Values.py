import numpy as np

salary = np.array([
350000,
450000,
np.nan,
1200000,
400000,
np.nan,
1800000,
950000,
550000,
750000
])

# Find missing values
missing = np.isnan(salary)
print(missing)

# Count missing values
count_missing = np.isnan(salary).sum()
print(count_missing)

# Replace missing values with the mean salary
mean_salary = np.nanmean(salary)
print(mean_salary)

salary[np.isnan(salary)] = mean_salary
print(salary)