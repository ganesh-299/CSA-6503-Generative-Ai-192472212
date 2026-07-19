import matplotlib.pyplot as plt

students = ["Ganesh", "Rahul", "Priya", "Anil", "Kiran"]
marks = [85, 92, 78, 88, 95]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()