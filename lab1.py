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

    for key in range(1, len(btext) + 1):
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
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        
if choice == 1:
    plaintext = input("Enter plaintext: ")
    n = int(input("Enter key: "))
    print("Ciphertext: ",encrypt(plaintext,n))
elif choice == 2:
    plaintext = input("Enter plaintext: ")
    n = int(input("Enter key: "))
    print("Ciphertext: ",decrypt(plaintext,n))
elif choice == 3: 
    plaintext = input("Enter plaintext: ")
    print("Ciphertext: ",brutefore(plaintext))