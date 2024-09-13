def encrypt(etext,n):
    encrypted = ""
    for i in range(len(etext)):
        ch = etext[i]
        if ch==" ":
            encrypted+=" "
        elif (ch.isupper()):
            encrypted += chr((ord(ch) + n-65) % 26 + 65)        
        else:
            encrypted += chr((ord(ch) + n-97) % 26 + 97)
    return encrypted

def decrypt(dtext,n):        
    decrypted = ""
    for i in range(len(dtext)):
        ch = dtext[i]
        if ch==" ":
            decrypted+=" "
        elif (ch.isupper()):
            decrypted += chr((ord(ch) - n - 65) % 26 + 65)        
        else:
            decrypted += chr((ord(ch) - n - 97) % 26 + 97)
    return decrypted

def brutefore(btext):
    for key in range(1, 25):
        brutetext = ''
        for i in range(len(btext)):
            ch = btext[i]
            if ch == " ":
                brutetext += " "
            elif (ch.isupper()):
                brutetext += chr((ord(ch) + key - 65) % 26 + 65)        
            else:
                brutetext += chr((ord(ch) + key - 97) % 26 + 97)
        print('Key #%s: %s' % (key, brutetext))

print("Choose an option:")
print("1. Encryption")
print("2. Decryption")
print("3. Brute Force")
while True:
    try:
        choice = int(input("Enter your choice (1/2/3): "))
        if choice not in [1, 2, 3]:
            raise ValueError("Choice must be 1, 2, or 3.")
        break
    except ValueError as e:
        print("Invalid input. Please enter 1, 2, or 3.")

while True:
    try:
        plaintext = input("Enter plaintext: ")
        if plaintext == "": 
            raise ValueError("Plaintext cannot be empty.")
        break
    except ValueError as e:
        print("Invalid input. Please enter an text for plaintext.")

while True:
    try:
        n = int(input("Enter key: "))
        if n == 0 or n >26: 
            raise ValueError("Key cannot be 0.")
        break
    except ValueError as e:
        print("Invalid input. Please enter an int for key.")

if choice == 1:
    print("Ciphertext:",encrypt(plaintext,n))
elif choice == 2:
    print("Ciphertext:",decrypt(plaintext,n))
elif choice == 3: 
    print(brutefore(plaintext))
