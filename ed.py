import base64

def encryption(key,plain):
    cipher = []
    for i in range(len(plain)):
        keybuffer = key[(i%len(key))]
        cipherbuffer = chr(ord(plain[i]) + ord(keybuffer) % 256)
        cipher.append(cipherbuffer)
    return "".join(cipher)

def decryption(key,cipher):
    plain = []
    for i in range(len(cipher)):
        keybuffer = key[(i%len(key))]
        plainbuffer = chr((256 + ord(cipher[i]) - ord(keybuffer)) %256)
        plain.append(plainbuffer)
    return "".join(plain)

def crypt(key,message,flag):
    if flag:
        return encryption(key,message)
    else:
        return decryption(key,message)

key = raw_input("Enter key")
message = raw_input("")
cipher = crypt(key,message,True)
print(base64.urlsafe_b64encode(cipher))
print(crypt(key,cipher,False))
