import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 18000, 17000, 20000, 22000]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.grid(True)

plt.show()