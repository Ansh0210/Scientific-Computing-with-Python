def convert_to_snake_case(pascal_or_camel_cased_string):
    # The commented-out part below is an alternative implementation that does not use list comprehension.
    # It achieves the same result by iterating through each character in the string and building the snake_case string step by step.
    """ 
    # Initialize an empty list to hold the snake_cased characters.
    snake_cased_char_list = []
    # Iterate through each character in the input string.
    for char in pascal_or_camel_cased_string:
        # Check if the character is uppercase.
        if char.isupper():
            # If it is uppercase, prepend an underscore and convert the character to lowercase.
            converted_character = '_' + char.lower()
            # Append the converted character to the list.
            snake_cased_char_list.append(converted_character)
        else:
            # If the character is not uppercase, append it as is to the list.
            snake_cased_char_list.append(char)
    # Join the characters in the list to form the snake_cased string.
    snake_cased_string = ''.join(snake_cased_char_list)
    # Strip leading underscores from the string (for PascalCase input).
    clean_snake_cased_string = snake_cased_string.strip('_')
    # Return the cleaned snake_cased string.
    return clean_snake_cased_string 
    """
    
    # Below is the part that uses list comprehension to achieve the same result more succinctly.
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # Prepend '_' and convert to lower if the character is uppercase.
        else char  # Keep the character as is if it's not uppercase.
        for char in pascal_or_camel_cased_string  # Iterate over each character in the input string.
    ]

    # Join the list into a string and strip leading underscores (for PascalCase input).
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Example usage of the convert_to_snake_case function.
    print(convert_to_snake_case('ALongAndComplexString'))

if __name__ == '__main__':
    main()
