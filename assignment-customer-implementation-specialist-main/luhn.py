def is_valid_credit_card(number):
    number = number.replace(' ', '')  # Remove any spaces from the input

    # Check if the number contains only digits
    if not number.isdigit():
        return False

    # Double every second digit starting from the right
    digits = [int(x) for x in number]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] = (digits[i] * 2) % 10 + (digits[i] * 2) // 10

    # Sum all the digits
    total = sum(digits)

    # Check if the total is divisible by 10
    return total % 10 == 0

def main():
    # Prompt the user for input
    credit_card_number = input("Enter a credit card number: ")

    # Check if the credit card number is valid
    if is_valid_credit_card(credit_card_number):
        print("Valid credit card number.")
        exit(0)
    else:
        print("Invalid credit card number.")
        exit(42)

if __name__ == "__main__":
    main()

