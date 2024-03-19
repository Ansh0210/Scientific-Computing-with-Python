# Define a function to verify the validity of a credit card number using the Luhn algorithm.
def verify_card_number(card_number):
    sum_of_odd_digits = 0  # Initialize sum for odd digits (from right, 0-based indexing).
    card_number_reversed = card_number[::-1]  # Reverse the card number to process digits.
    odd_digits = card_number_reversed[::2]  # Extract odd indexed digits from the reversed number.

    # Sum up all the odd digits (considering original positions).
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0  # Initialize sum for even digits.
    even_digits = card_number_reversed[1::2]  # Extract even indexed digits from the reversed number.
    
    # Double each even digit and sum them, subtracting 9 from numbers greater than 9.
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)  # Adjust numbers greater than 9.
        sum_of_even_digits += number
    
    total = sum_of_odd_digits + sum_of_even_digits  # Calculate the total sum of digits.
    return total % 10 == 0  # Check if the total modulo 10 is equal to 0 (valid if true).

# Main function to test the card number validity.
def main():
    card_number = '4111-1111-4555-1142'  # Example card number.
    # Remove dashes and spaces from the card number for processing.
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Verify the card number and print whether it's valid or not.
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Call the main function to execute the program.
if __name__ == '__main__':    
    main()  
