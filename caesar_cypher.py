# This function encrypts a message using the Caesar cipher
def crypt_function():
    # This loop will continue until the user enters a valid shift value
    true = True
    while(true):
        # The alphabet used for the cipher
        alphabet = ('abcdefghijklmnopqrstuvwxyz')
        # The encrypted message will be stored in this variable
        encrypted_text = ""
        # The user is prompted to enter a message to encrypt
        raw = input("Enter a message: ")
        # The user is prompted to enter a shift value
        shift = int(input("Insert a value from 1-26: "))
        
        # If the shift value is not between 1 and 26, the user is asked to enter it again
        if shift > 26 or shift < 1:
            print("No, man, seriously...")
        else:
            # Each character in the message is shifted by the shift value to encrypt it
            for char in raw.lower():
                if char == " ":
                    encrypted_text += char
                else:
                    index = alphabet.find(char)
                    new_index = (index + shift) % len(alphabet)
                    encrypted_text += alphabet[new_index]
            # The original and encrypted messages are printed
            print('plain text:', raw)
            print('encrypted text:', encrypted_text)
            print("\n")
            # The loop is exited
            true = False


# This function decrypts a message encrypted with the Caesar cipher
def decrypt_function():
    # This loop will continue until the user enters a valid shift value
    loop = True
    while (loop):
        # The alphabet used for the cipher
        alphabet = ('abcdefghijklmnopqrstuvwxyz')
        # The decrypted message will be stored in this variable
        encrypted_text = ""
        # The user is prompted to enter a message to decrypt
        raw = input("Enter a message: ")
        # The user is prompted to enter the shift value used to encrypt the message
        shift = int(input("Insert a value from 1-26: "))
        
        # If the shift value is not between 1 and 26, the user is asked to enter it again
        if shift > 26 or shift < 1:
            print("No, man, seriously...")
        else:
            # Each character in the message is shifted by the negative of the shift value to decrypt it
            for char in raw.lower():
                if char == " ":
                    encrypted_text += char
                else:
                    index = alphabet.find(char)
                    new_index = (index - shift) % len(alphabet)
                    encrypted_text += alphabet[new_index]
            # The original and decrypted messages are printed
            print('plain text:', raw)
            print('encrypted text:', encrypted_text)
            print("\n")
            # The loop is exited
            loop = False


# This function allows the user to choose between encrypting and decrypting a message
def crypt_or_decrypt():
    # This loop will continue until the user chooses to quit
    true_main = True
    while (true_main):
        # The user is prompted to choose an option
        crypt = int(input("Enter 1 to crypt your message, enter 2 to decrypt your message or enter 0 to quit : "))
        # If the user chooses 1, the vigenere function is called to encrypt a message
        if crypt == 1:
            crypt_function()
        # If the user chooses 2, the decrypt_function is called to decrypt a message
        elif crypt == 2:
            decrypt_function()
        # If the user chooses 0, the loop is exited and the program ends
        elif crypt == 0:
            true_main = False
        # If the user enters an invalid choice, they are asked to enter it again
        else:
            print("Invalid choice")
        

# The crypt_or_decrypt function is called to start the program
crypt_or_decrypt()
