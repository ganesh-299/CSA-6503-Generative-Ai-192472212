import numpy as np

sales = np.array([
    [12000, 15000, 18000],
    [14000, 16000, 17000],
    [10000, 12000, 13000],
    [18000, 20000, 22000]
])

print("Monthly Sales")
print(sales)

print("\nTotal Sales of Each Employee")
print(np.sum(sales, axis=1))

print("\nMonthly Total Sales")
print(np.sum(sales, axis=0))

print("\nAverage Sales")
print(np.mean(sales))

print("\nHighest Sale")
print(np.max(sales))

print("\nLowest Sale")
print(np.min(sales))

print("\nEmployees with Total Sales Greater Than 45000")

totals = np.sum(sales, axis=1)

for i in range(len(totals)):
    if totals[i] > 45000:
        print("Employee", i + 1, ":", totals[i])