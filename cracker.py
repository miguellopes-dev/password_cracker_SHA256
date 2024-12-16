import hashlib

#Method to convert the password.txt passwords into the SHA256 hash

def password_to_sha256(text):
    digest = hashlib.sha256(
        text.encode() #Encoding string is needed for it to work
    ).hexdigest()  #Returns back the 64 character hexadecimal format string (it's a 32 bytes string at this point)
    return digest



def main():
    user_sha256 = input("SHA256 to crack: ")
    cleaned_user_sha256 = user_sha256.strip().lower()  #We have to clean inputs to get rid of spaces in order to avoid any mistakes and we also have to turn in lower case because when we call above the hexdigest function, it returns the hash in lower case   

#Load the passwords file and make it iterate on each line

    with open("./passwords.txt") as f:
        for line in f:
            password = line.strip()     #Again getting rid of any possible spaces
            converted_sha256 = password_to_sha256(password)            
            if cleaned_user_sha256 == converted_sha256:
                print(f"Password found: {password}")
                return
    print("We could not find the password")



if __name__ == '__main__':
    main()