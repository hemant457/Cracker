import base64

# Helper Functions for Encoding/Decoding
def encode_to_rotn(text, n):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - 97 + n) % 26 + 97))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - 65 + n) % 26 + 65))
        else:
            result.append(char)
    return ''.join(result)

def decode_from_rotn(text, n):
    return encode_to_rotn(text, -n)

def encode_to_rot5(text):
    return ''.join(chr((ord(char) - 48 + 5) % 10 + 48) if '0' <= char <= '9' else char for char in text)

def decode_from_rot5(text):
    return encode_to_rot5(text)

def encode_to_rot18(text):
    return ''.join(
        chr((ord(char) - 97 + 13) % 26 + 97) if 'a' <= char <= 'z' else
        chr((ord(char) - 65 + 13) % 26 + 65) if 'A' <= char <= 'Z' else
        chr((ord(char) - 48 + 5) % 10 + 48) if '0' <= char <= '9' else
        char for char in text
    )

def decode_from_rot18(text):
    return encode_to_rot18(text)

def encode_to_rot47(text):
    return ''.join(chr(33 + (ord(char) - 33 + 47) % 94) if 33 <= ord(char) <= 126 else char for char in text)

def decode_from_rot47(text):
    return encode_to_rot47(text)

def encode_to_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_from_base64(text):
    return base64.b64decode(text).decode()

def encode_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def decode_from_binary(text):
    return ''.join(chr(int(b, 2)) for b in text.split())

def encode_to_decimal(text):
    return ' '.join(str(ord(c)) for c in text)

def decode_from_decimal(text):
    return ''.join(chr(int(d)) for d in text.split())

def encode_to_hexadecimal(text):
    return ' '.join(format(ord(c), 'x') for c in text)

def decode_from_hexadecimal(text):
    return ''.join(chr(int(h, 16)) for h in text.split())

# Main Menu
def main():
    while True:
        print("\nWelcome to the Encoding-Decoding Tool!")
        print("What do you want to do?")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter the text to encode: ")
            print("\nChoose an encoding method:")
            print("1. Binary")
            print("2. Decimal")
            print("3. Hexadecimal")
            print("4. Base64")
            print("5. ROTn (Custom)")
            print("6. ROT5")
            print("7. ROT18")
            print("8. ROT47")
            method = input("Enter your choice (1-8): ")

            if method == '1':
                print("Encoded to Binary:", encode_to_binary(text))
            elif method == '2':
                print("Encoded to Decimal:", encode_to_decimal(text))
            elif method == '3':
                print("Encoded to Hexadecimal:", encode_to_hexadecimal(text))
            elif method == '4':
                print("Encoded to Base64:", encode_to_base64(text))
            elif method == '5':
                n = int(input("Enter the ROT value (e.g., 13 for ROT13): "))
                print(f"Encoded to ROT{n}:", encode_to_rotn(text, n))
            elif method == '6':
                print("Encoded to ROT5:", encode_to_rot5(text))
            elif method == '7':
                print("Encoded to ROT18:", encode_to_rot18(text))
            elif method == '8':
                print("Encoded to ROT47:", encode_to_rot47(text))
            else:
                print("Invalid choice! Please try again.")

        elif choice == '2':
            text = input("Enter the text to decode: ")
            print("\nChoose a decoding method:")
            print("1. Binary")
            print("2. Decimal")
            print("3. Hexadecimal")
            print("4. Base64")
            print("5. ROTn (Custom)")
            print("6. ROT5")
            print("7. ROT18")
            print("8. ROT47")
            method = input("Enter your choice (1-8): ")

            if method == '1':
                print("Decoded from Binary:", decode_from_binary(text))
            elif method == '2':
                print("Decoded from Decimal:", decode_from_decimal(text))
            elif method == '3':
                print("Decoded from Hexadecimal:", decode_from_hexadecimal(text))
            elif method == '4':
                print("Decoded from Base64:", decode_from_base64(text))
            elif method == '5':
                n = int(input("Enter the ROT value (e.g., 13 for ROT13): "))
                print(f"Decoded from ROT{n}:", decode_from_rotn(text, n))
            elif method == '6':
                print("Decoded from ROT5:", decode_from_rot5(text))
            elif method == '7':
                print("Decoded from ROT18:", decode_from_rot18(text))
            elif method == '8':
                print("Decoded from ROT47:", decode_from_rot47(text))
            else:
                print("Invalid choice! Please try again.")

        elif choice == '3':
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
