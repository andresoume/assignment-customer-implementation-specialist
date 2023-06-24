# Luhn Validator

Please provide any additional information about your assignment here.

This assignment has been completed by Andre Soume as a test for the position of customer implementation specialist at Source.ag

Disclaimer: StackOverflow and ChatGPT have been used to aid me in completing this assignment. 

High level explaination of each part of the code:

1. The `is_valid_credit_card` function takes a credit card number as input and checks if it's valid based on the Luhn algorithm.
2. The first step is to remove any spaces from the input number using the `replace` method. This allows us to handle credit card numbers with or without spaces.
3. We then check if the number contains only digits using the `isdigit` method. If it contains any non-digit characters, we immediately return `False`.
4. Next, we convert each digit in the number from a string to an integer and store them in a list called `digits`.
5. Starting from the second-to-last digit and moving towards the left, we double every second digit. If the result is greater than 9, we split it into its individual digits and add them together. For example, 12 becomes 1 + 2 = 3.
6. After doubling and splitting the digits, we update the corresponding positions in the `digits` list.
7. Once we have processed all the digits, we calculate the sum of all the numbers in the `digits` list.
8. Finally, we check if the total sum is divisible by 10. If it is, the credit card number is valid according to the Luhn algorithm, so we return `True`. Otherwise, we return `False`.
9. The `main` function is the entry point of our application.
10. It prompts the user to enter a credit card number using the `input` function.
11. It then calls the `is_valid_credit_card` function with the user-provided number to check its validity.
12. If the credit card number is valid, it prints "Valid credit card number" and exits with status 0 using `sys.exit(0)`.
13. If the credit card number is invalid, it prints "Invalid credit card number" and exits with status 42 using `sys.exit(42)`.
14. The `if __name__ == "__main__":` condition ensures that the `main` function is only executed when the script is run directly, not when it's imported as a module.

So basically: It takes the user's input, applies the Luhn algorithm to validate the credit card number, and provides a result accordingly.

Note: No matter what I tried, I could not get the test script to run. 
