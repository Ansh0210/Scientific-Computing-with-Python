# Define the function 'caesar' to encrypt a message using Caesar cipher technique
def caesar(message, offset):
    # Define the alphabet to be used in the encryption. This only includes lowercase letters.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Initialize an empty string to hold the encrypted text.
    encrypted_text = ''

    # Convert the entire message to lowercase to standardize the encryption process,
    # since the alphabet is defined in lowercase letters.
    for char in message.lower():
        # Check if the character is a space. If so, add it directly to the encrypted text
        # without encrypting it. This keeps spaces as is in the encrypted message.
        if char == ' ':
            encrypted_text += char
        else:
            # Find the index of the current character in the alphabet string.
            index = alphabet.find(char)
            # Calculate the new index by adding the offset to the current index.
            # Use modulo by the length of the alphabet to wrap around if the new index
            # goes beyond the alphabet length (e.g., 'z' shifted by 1 becomes 'a').
            new_index = (index + offset) % len(alphabet)
            # Append the character at the new index in the alphabet to the encrypted text.
            encrypted_text += alphabet[new_index]
    
    # After processing all characters, print the original (plain text) message.
    print('plain text:', message)
    # Print the resulting encrypted text.
    print('encrypted text:', encrypted_text)

# Example usage of the 'caesar' function.
# Encrypt the message 'Hello Kevin' with a shift of 3.
text = 'Hello Kevin'
shift = 3
caesar(text, shift)

# Encrypt the same message 'Hello Kevin' with a shift of 13, demonstrating how
# different shifts result in different encrypted messages.
caesar(text, 13)