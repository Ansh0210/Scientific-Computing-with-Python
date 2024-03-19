# Define the encrypted text and the custom key for decryption.
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Define the Vigenère cipher function.
def vigenere(message, key, direction=1):
    key_index = 0  # Initialize the key index to track the position within the key.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Define the alphabet used for the cipher.
    final_message = ''  # Initialize an empty string for the final message.

    # Loop through each character in the message.
    for char in message.lower():  # Convert message to lowercase to handle uppercase letters.

        # Append any non-letter character directly to the final message.
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to use for encoding or decoding.
            key_char = key[key_index % len(key)]  # Use modulo to wrap around the key.
            key_index += 1  # Move to the next character in the key.

            # Calculate the offset using the current key character.
            offset = alphabet.index(key_char)
            # Find the current character's index in the alphabet.
            index = alphabet.find(char)
            # Calculate the new index for encryption/decryption, adjusting direction.
            new_index = (index + offset * direction) % len(alphabet)
            # Append the encrypted/decrypted character to the final message.
            final_message += alphabet[new_index]
    
    return final_message  # Return the final encrypted/decrypted message.

# Function to encrypt a message using the Vigenère cipher.
def encrypt(message, key):
    return vigenere(message, key)  # Encrypt using direction=1 by default.
    
# Function to decrypt a message using the Vigenère cipher.
def decrypt(message, key):
    return vigenere(message, key, -1)  # Decrypt by reversing the direction.

# Display the encrypted text and the key.
print(f'\nEncrypted text: {text}')
print(f'\nKey: {custom_key}')

# Decrypt the message and display the original text.
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n') 
