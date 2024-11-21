
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initialize an empty list to store the matrix
matrix = []

# Loop to input each row
for i in range(rows):
    # Take input for each row and convert it into a list of integers
    row = list(map(int, input(f"Enter the elements of row {i + 1} (space-separated): ").split()))
    if len(row) != cols:
        print(f"Please enter exactly {cols} elements.")
        break
    matrix.append(row)

# List to store the sum of each row
out = []

# Calculate the sum of each row
for row in matrix:
    summ = 0
    for value in row:
        summ += value
    out.append(summ)

# Print the output
print("Sum of each row:", out)
