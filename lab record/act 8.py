import numpy as np

array_3x3 = np.random.randint(1, 21, size=(3, 3))

print("Original 3x3 Array:")
print(array_3x3)

array_mean = np.mean(array_3x3)
print("\nMean of the array:", array_mean)

array_3x3[array_3x3 < 10] = 0

print("\nModified 3x3 Array (elements < 10 replaced with 0):")
print(array_3x3)