import matplotlib.pyplot as plt

subjects = ["Python", "Java", "AI", "DBMS", "OS"]
hours = [10, 8, 12, 6, 4]

plt.pie(hours,
        labels=subjects,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Study Time Distribution")

plt.show()