import numpy as np

salary = np.array([35000, 42000, 55000, 61000, 48000, 72000])

print("Employee Salaries:")
print(salary)

print("\nTotal Salary:")
print(np.sum(salary))

print("\nAverage Salary:")
print(np.mean(salary))

print("\nHighest Salary:")
print(np.max(salary))

print("\nLowest Salary:")
print(np.min(salary))

print("\nSorted Salaries:")
print(np.sort(salary))

print("\nEmployees earning more than 50000:")

for s in salary:
    if s > 50000:
        print(s)