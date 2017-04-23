import base64

def encryption(key,plain) :
    cipher = []
    for i in range(len(plain)) :
        keybuffer = key[(i % len(key))]
        cipherbuffer = chr(ord(plain[i]) + ord(keybuffer) % 256)
        cipher.append(cipherbuffer)
    return "".join(cipher)

def decyption(key,cipher) :
    plain = []
    for i in range(len(cipher)) :
        keybuffer = key[(i % len(key))]
        plainbuffer = chr((256 + ord(cipher[i]) - ord(keybuffer)) % 256)
        plain.append(plainbuffer)
    return "".join(plain)

def crypt(key,message,option) :
    if option is True :
        return encryption(key,message)
    else :
        return decyption(key,message)

print("Enter key: ")
key = raw_input()
print("\nEnter your message: ")
plain = raw_input()
print("\nEncrypted message is: ")
cipher = crypt(key,plain,True)
print(base64.urlsafe_b64encode(cipher))
print("\nDecrypted message: ")
plain = crypt(key,cipher,False)
print(plain)
