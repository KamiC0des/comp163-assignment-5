print("=== Challenge 2: Prime Number Checker ===")

user_num = int(input("Enter a number: ")) # Takes a positive integer from the user
print(f"Testing divisors from 2 to {user_num - 1}...")

# Gets numbers between 2 and the value of user_num - 1
for i in range(2, user_num - 1):
    # Checks if the user's number is evenly divisible by the value of i
    if user_num % i == 0:
        # if user_num is evenly divisible by i, it prints that user_num is not prime and exits the loop
        print(f"{user_num} is not prime (divisible by {i})")
        break
else:
    # If user_num is a prime number, it prints that the number is prime
    print(f"{user_num} is prime!")