# comp163-assignment-5

# CHALLENGE 1
LOOP USED:

For this challenge, I used a while loop. I chose to use this loop type because the number of steps is unknown, so I need to use a while loop to count how many times the loop iterates. The loop continue until the sequence reaches 1.

HOW IT WORKS:
1. Start with a positive integer given by the user.
2. If the number is even, divide it by 2; if it’s odd, multiply it by 3 and add 1.
3. Continue looping until the number becomes 1.
4. Track and print the sequence and the total number of steps.
   
# CHALLENGE 2
LOOP USED:

For this challenge, I used a for loop. I chose to use this loop type because the number of possible divisiors to check from is known (2 to user_num - 1).

HOW IT WORKS:
1. The user enters a number (user_num).
2. The program tests divisors from 2 up to user_num - 1.
3. If any divisor evenly divides the number (user_num % i == 0), the program prints that the number is not prime and stops checking further (using break).
4. If no divisor is found, the for loop completes normally and else executes, printing that the number is prime.

# CHALLENGE 3
LOOPS USED:

For this challenge, I used a nested for loop. I chose to use this loop type because both the rows and columns have a known range (1 to 10).

HOW IT WORKS:
1. The program prints a header row containing the numbers 1–10.
2. The outer for loop begins, starting with row = 1 and running through row = 10.
3. For each row:
  - Print the row label with (:2) to ensure proper spacing.
  - The program prints the row label (e.g., 1, 2, …, 10) aligned to the left.
  - The inner for loop runs from column = 1 through 10.
  - For each column, the product is calculated (row × col) and printed with         proper spacing (:4) to keep the table aligned.
4. Move to the next line after finishing each row.

# AI ASSISTANCE

For all challenges, I had a few errors that I couldn't point out. I used ChatGPT to debug my code and fix my syntax.
