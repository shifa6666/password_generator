import random
import string

def generate_password(length):
    if length < 4:  # Ensures a minimum length to have a strong password
        print("Password length should be at least 4")
        return None

    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one character from each character set
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random choices from the character set
    password += random.choices(characters, k=length-4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

