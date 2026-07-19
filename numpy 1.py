import numpy as np

marks = np.array([
    [85, 90, 78],
    [76, 88, 92],
    [90, 85, 89],
    [65, 70, 75],
    [95, 98, 97]
])

print("Student Marks:")
print(marks)

print("\nTotal Marks:")
total = np.sum(marks, axis=1)
print(total)

print("\nAverage Marks:")
average = np.mean(marks, axis=1)
print(average)

print("\nHighest Marks:")
highest = np.max(marks, axis=1)
print(highest)

print("\nLowest Marks:")
lowest = np.min(marks, axis=1)
print(lowest)

print("\nStudents scoring above 80 average:")
for i in range(len(average)):
    if average[i] > 80:
        print("Student", i + 1, "Average =", average[i])