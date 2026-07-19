import numpy as np

numbers = np.random.randint(1, 101, 20)

print("Random Numbers")
print(numbers)

print("\nSorted Numbers")
print(np.sort(numbers))

print("\nMaximum")
print(np.max(numbers))

print("\nMinimum")
print(np.min(numbers))

print("\nAverage")
print(np.mean(numbers))

print("\nEven Numbers")
for i in numbers:
    if i % 2 == 0:
        print(i)

print("\nOdd Numbers")
for i in numbers:
    if i % 2 != 0:
        print(i)