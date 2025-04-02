def find_largest_five():
  print("Find the largest of five numbers")
  numbers = []
  for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

  largest = numbers[0] 
  for num in numbers:
    if num > largest:
      largest = num

  print(f"The largest number is: {largest}")

find_largest_five()