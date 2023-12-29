import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special_chars else ""

    # Combine character sets based on user preferences
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure the password length is at least 4 characters
    length = max(4, length)

    # Generate the password
    password = random.sample(all_chars, length)
    password = ''.join(password)

    return password

def main():
    while True:
        desired_length = int(input("Enter the desired password length: "))
        password = generate_password(length=desired_length)
        print("Random Password:", password)

        generate_again = input("Generate another password? (yes/no): ").lower()
        if generate_again != "yes":
            print("Exiting password generator.")
            break

if __name__ == "__main__":
    main()
