import numpy as np
import random

def matrix_operations_3x3():
  
  matrix_A = np.random.randint(1, 11, size=(3, 3))
  matrix_B = np.random.randint(1, 11, size=(3, 3))

  print("Matrix A:")
  print(matrix_A)

  print("\nMatrix B:")
  print(matrix_B)

  matrix_subtraction = np.subtract(matrix_A, matrix_B)
  print("\nMatrix Subtraction (A - B):")
  print(matrix_subtraction)

  matrix_division = np.divide(matrix_A, matrix_B)
  print("\nElement-wise Matrix Division (A / B):")
  print(matrix_division)

matrix_operations_3x3()