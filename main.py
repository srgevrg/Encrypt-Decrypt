import string

def encrypt(text, shift):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]
    mapping = str.maketrans(lower + upper, shifted_lower + shifted_upper)
    return text.translate(mapping)

def decrypt(text, shift):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]
    mapping = str.maketrans(shifted_lower + shifted_upper, lower + upper)
    return text.translate(mapping)

while True:
    action = input("Would you like to (e)ncrypt or (d)ecrypt? ")
    if action == "e":
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift (1-26): "))
        result = encrypt(text, shift)
        print(f"Encrypted text: {result}")
    elif action == "d":
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift (1-26): "))
        result = decrypt(text, shift)
        print(f"Decrypted text: {result}")
    else:
        print("Invalid action. Exiting.")
        break

while True:
    action = input("Would you like to (e)ncrypt or (d)ecrypt? ")
