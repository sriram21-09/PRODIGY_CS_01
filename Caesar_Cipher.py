def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            code = ord(char) + shift_amount
            if char.islower():
                if code > ord('z'):
                    code -= 26
                result += chr(code)
            elif char.isupper():
                if code > ord('Z'):
                    code -= 26
                result += chr(code)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted = encrypt(message, shift)
print(f"Encrypted message: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted message: {decrypted}")
