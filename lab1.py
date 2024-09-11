def encrypt(etext,n):
    ans = ""
    for i in range(len(etext)):
        ch = etext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans

def decrypt(dtext,n):        
    letters="abcdefghijklmnopqrstuvwxyz"    
    decrypted_message = ""

    for ch in dtext:

        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - n) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch

def brutefore(btext):
    letters="abcdefghijklmnopqrstuvwxyz"    

    for key in range(len(letters)):
        translated = ''
        for ch in btext:
            if ch in letters:
                num = letters.find(ch)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            else:
                translated = translated + ch

print("Choose an option:")
print("1. Encryption")
print("2. Decryption")
print("3. Brute Force")
choice = int(input("Enter your choice (1/2/3): "))

plaintext = input("Enter plaintext: ")
n = int(input("Enter key: "))

if choice == 1:
    print("Ciphertext: ",encrypt(plaintext,n))
elif choice == 2:
    print("Ciphertext: ",decrypt(plaintext,n))
elif choice == 3:
    print("Ciphertext: ",brutefore(plaintext))


    