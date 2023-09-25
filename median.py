"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)



total = len(numbers)
numbers.sort()

if total % 2 == 0:
	median1 = numbers[total//2]
	median2 = numbers[total//2 - 1]
	median = (median1 + median2)/2
else:
	median = numbers[total//2]
print("Median is: " + str(median))
