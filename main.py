def encode(user_password):
    encoded_password = ""
    for char in user_password:
        char = int(char)
        char += 3
        char = str(char)
        encoded_password = encoded_password + char

    print(encoded_password)

def decode():
    # hi monica! :)
    pass

def main():
    # menu
    user_password = input("Please enter numerical string to be encoded or decoded: ")
    user_choice = input("1. Encode\n2. Decode\n")
    if user_choice == "1":
        encode(user_password)
    elif user_choice == "2":
        decode(user_password)


if __name__ == '__main__':
    main()