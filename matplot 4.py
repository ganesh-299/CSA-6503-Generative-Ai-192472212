import matplotlib.pyplot as plt

age = [18, 19, 20, 21, 22, 23, 24]
salary = [20000, 22000, 25000, 27000, 30000, 32000, 35000]

plt.scatter(age, salary)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.grid(True)

plt.show()