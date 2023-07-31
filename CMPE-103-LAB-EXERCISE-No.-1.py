def encrypt_string(input_string):
    encryption_dict = {'a': '*', 'e': '&', 'i': '#', 'o': '+', 'u': '!'}
    encrypted_string = ''

    for char in input_string:
        if char.lower() in encryption_dict:
            encrypted_string += encryption_dict[char.lower()]
        else:
            encrypted_string += char

    return encrypted_string


def main():
    input_string = input("Enter a string to encrypt: ")
    encrypted_string = encrypt_string(input_string)
    print("Encrypted string:", encrypted_string)


if __name__ == "__main__":
    main()
