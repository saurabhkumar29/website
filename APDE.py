import base64

def encryption(key,message) :
    cipherTextCharacters = []
    for i in range(len(message)) :
        keyForCurrentCharacter = key[(i % len(key))]
        currentCipherTextCharacter = chr(ord(message[i]) + ord(keyForCurrentCharacter) % 256)
        cipherTextCharacters.append(currentCipherTextCharacter)
    cipherText = "".join(cipherTextCharacters)
    return cipherText

def decryption(key,cipherText) :
    decryptedTextCharacters = []
    for i in range(len(cipherText)) :
        keyForCurrentCharacter = key[(i % len(key))]
        currentDecryptedTextCharacter = chr((256 + ord(cipherText[i]) - ord(keyForCurrentCharacter)) % 256)
        decryptedTextCharacters.append(currentDecryptedTextCharacter)
    decryptedText = "".join(decryptedTextCharacters)
    return decryptedText

print("Enter your password (i.e. key) - ")
key = raw_input()
print("")
print("Enter your message to be encrypted - ")
message = raw_input()
print("")
print("This is the cipher text generated - which can totally not be cracked ;) - ")
cipherText = vigenereEncryptionUsedToMeanSomethingBackInTheDay(key,message)
gibberish = base64.urlsafe_b64encode(cipherText)
print(gibberish)
print("")
print("This is the decrypted message using your password which is supposed to match your original message - ")
decryptedText = vigenereDecryptionUsedToMeanSomethingBackInTheDay(key,cipherText)
print(decryptedText)
print("")
