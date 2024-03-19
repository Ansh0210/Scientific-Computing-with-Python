# Import necessary modules
import re  # Regular expressions for pattern matching
import secrets  # Secure random numbers for managing secrets
import string  # Common string operations

# Define the function to generate a password
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a secure password.

    Args:
        length (int): Length of the password. Default is 16 characters.
        nums (int): Minimum number of numeric digits in the password.
        special_chars (int): Minimum number of special characters in the password.
        uppercase (int): Minimum number of uppercase letters in the password.
        lowercase (int): Minimum number of lowercase letters in the password.

    Returns:
        str: The generated password.
    """

    # Define the possible characters for the password
    letters = string.ascii_letters  # A string containing all ASCII letters (both uppercase and lowercase)
    digits = string.digits  # A string containing all numeric digits
    symbols = string.punctuation  # A string containing all special characters

    # Combine all possible characters into one string
    all_characters = letters + digits + symbols

    # Keep generating passwords until one meets all constraints
    while True:
        password = ''
        # Generate a random password of the specified length
        for _ in range(length):
            password += secrets.choice(all_characters)  # Choose a random character
        
        # Define constraints as tuples of (minimum count, regex pattern)
        constraints = [
            (nums, r'\d'),  # At least 'nums' digits
            (special_chars, fr'[{symbols}]'),  # At least 'special_chars' special characters
            (uppercase, r'[A-Z]'),  # At least 'uppercase' uppercase letters
            (lowercase, r'[a-z]')  # At least 'lowercase' lowercase letters
        ]

        # Check if the generated password meets all constraints
        if all(
            constraint <= len(re.findall(pattern, password))  # Find all occurrences matching the pattern
            for constraint, pattern in constraints
        ):
            break  # If all constraints are met, stop generating passwords
    
    return password  # Return the valid password
    
# If the script is run directly, generate a password and print it
if __name__ == '__main__':
    new_password = generate_password()  # Generate a new password
    print('Generated password:', new_password)  # Print the generated password
