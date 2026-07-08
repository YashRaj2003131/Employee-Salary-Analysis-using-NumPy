# Employee-Salary-Analysis-using-NumPy
A NumPy-based employee salary analysis case study demonstrating array operations, statistics, Boolean indexing, reshaping, stacking, sorting, missing value handling, and outlier detection using Python.

This project demonstrates how to perform data analysis using **NumPy** by working with a synthetic employee salary dataset. It covers essential NumPy concepts such as statistical analysis, Boolean indexing, reshaping, stacking, sorting, missing value handling, and outlier detection.

The goal of this project is to strengthen fundamental NumPy skills that are commonly used in data analysis and data science.

---

## 🚀 Features

* Calculate descriptive statistics

  * Mean
  * Median
  * Standard Deviation
  * Variance
  * Minimum & Maximum Salary

* Filter data using Boolean Indexing

  * Employees earning above a specified salary
  * Employees satisfying multiple conditions

* Apply conditional operations

  * Award salary bonuses based on salary thresholds

* Reshape arrays

  * Convert arrays into different dimensions

* Stack arrays

  * Vertical Stacking (`vstack`)
  * Horizontal Stacking (`hstack`)
  * `stack(axis=0)`
  * `stack(axis=1)`

* Sort salary data

  * Ascending order
  * Descending order

* Handle missing values

  * Detect missing values
  * Count missing values
  * Replace missing values with the mean salary

* Detect outliers

  * Compare mean and median after introducing an outlier
  * Understand the effect of extreme values on statistical measures

---

## 🛠 Technologies Used

* Python 3
* NumPy

---

## 📂 Project Structure

```text
Employee-Salary-Analysis-NumPy/
│
├── salary_analysis.py
├── README.md
└── requirements.txt
```

---

## 📊 Concepts Covered

* NumPy Arrays
* Array Indexing & Slicing
* Boolean Indexing
* Vectorized Operations
* Statistical Functions
* Broadcasting
* Reshaping Arrays
* Array Stacking
* Sorting Arrays
* Missing Value Handling
* Outlier Analysis

---

## 📌 Sample Tasks

* Find the total number of employees.
* Calculate average and median salary.
* Find employees earning more than ₹700,000.
* Filter employees based on multiple conditions.
* Apply salary bonuses using Boolean indexing.
* Reshape salary arrays.
* Stack multiple department salary arrays.
* Sort salary data.
* Detect and replace missing values.
* Analyze the impact of outliers on the mean and median.

---

## 💡 Key Learnings

This project helped me understand how to:

* Perform efficient numerical computations using NumPy.
* Replace loops with vectorized operations.
* Analyze numerical datasets using statistical functions.
* Filter data using Boolean conditions.
* Manipulate arrays with reshaping and stacking.
* Handle missing values effectively.
* Detect and interpret outliers in a dataset.

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/employee-salary-analysis-numpy.git
```

2. Navigate to the project folder:

```bash
cd employee-salary-analysis-numpy
```

3. Install the required package:

```bash
pip install -r requirements.txt
```

4. Run the program:

```bash
python salary_analysis.py
```

---

## 📈 Future Improvements

* Read employee data from CSV files.
* Perform analysis using Pandas.
* Visualize salary trends with Matplotlib.
* Add interactive charts using Plotly.
* Expand the project with real-world datasets.

---

## 📷 Sample Output

```text
Total Employees: 10

Average Salary: ₹775,000

Median Salary: ₹650,000

Highest Salary: ₹1,800,000

Lowest Salary: ₹350,000

Employees earning more than ₹700,000:
[104 107 108 110]

Missing Values: 2

Mean after Outlier: ₹1,595,000

Median after Outlier: ₹650,000
```

---

## ⭐ Conclusion

This project provides hands-on practice with NumPy by solving real-world employee salary analysis tasks. It demonstrates how NumPy enables efficient numerical computing, statistical analysis, and data manipulation using vectorized operations, making it an excellent foundation for advanced data analytics and machine learning projects.

