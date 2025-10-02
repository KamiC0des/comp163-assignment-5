print("=== Challenge 3: Multiplication Table ===")

print("Multiplication Table:")
print("      1   2   3   4   5   6   7   8   9  10") # Prints header row with numbers 1-10
product = 0 # Sets starting value of product to 0

# Iterates through row numbers 1-10
for row in range(1, 11):
    # Prints current row number (1-10) with 2 spaces after
    print(f"{row:2}", end="")
    # Iterates through column numbers (1-10)
    for col in range(1, 11):
        # Assigns the product of the row and the column number to the variable 'product'
        product = row * col
        # Prints the product on the same line as the row with 4 spaces after
        print(f"{product:4}", end="")
    print()