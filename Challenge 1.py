print("=== Challenge 1: Collatz Conjecture ===")
pos_num = int(input("Enter starting number: ")) # Created to take a number from the user
step_count = 0 # Created to count how many times the loop iterates

print("Sequence:", end=" ") # Starts the sequence

# Checks if pos_num is not equal to 1
while pos_num != 1:
    print(pos_num, end=" ") # Prints the first value of pos_num

    if pos_num % 2 == 0: # Checks if pos_num is an even number
        pos_num //= 2 # If the number is even, it is divided by 2
    else:
        pos_num *= 3 # If the number is odd, it is multiplied by 3
        pos_num += 1 # and incremented
    step_count += 1

print(pos_num) # Prints the final '1' in the sequence

print("Steps:", step_count) # Prints the number of steps