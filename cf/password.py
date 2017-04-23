import base64

def encryption(key, message):
	encrypted = []
	for i in range(len(message)):
		key1 = key[(i%len(key))]
		encrypt = chr(ord(message[i]) + ord(key1)%256)
		encrypted.append(encrypt)
	encryptedText = "".join(encrypted)
	return encryptedText
def decryption(key, cipherText):
	decrypted = []
	for i in range(len(cipherText)):
		key1 = key[(i%len(key))]	
		decrypt = chr((256+ord(cipherText[i])-ord(key1))%256)
		decrypted.append(decrypt)
	decryptedText = "".join(decrypted)
	return decryptedText

print("Enter key")
key = raw_input()
print("")
print("Enter message")
message = raw_input()
print("")
print("encrypted text")
cipherText = encryption(key, message)
gibberish = base64.urlsafe_b64encode(cipherText)
print(gibberish)
print("")
print("decrypted message ")
decryptedText = decryption(key, cipherText)
print(decryptedText)
print("")
