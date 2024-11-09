import sys

# Get the number from command-line arguments
number = int(sys.argv[1])

# Loop through all numbers from 1 to the specified number
for i in range(1, number + 1):
    # Check if i is a divisor of number
    if number % i == 0:
        print(i, end=" ")

# Print a newline at the end
print()
