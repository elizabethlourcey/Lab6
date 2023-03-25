def encode(user_password):
    encoded_password = ""
    for char in user_password:
        char = int(char)
        char += 3
        char = str(char)
        encoded_password = encoded_password + char

    print(encoded_password)

def decode(user_password):
    # hi monica! :)
    # hi elizabeth!
    password_list = list(user_password)
    decoded_password_str = ""

    for element in password_list:
        element = int(element)
        element -= 3
        if element < 0:
            element += 10
        decoded_password_str += str(element)
    print(decoded_password_str)


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