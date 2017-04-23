import socket,sys

print("\nEnter the multiplicand and multiplier: ")
num1 = raw_input()
num2 = raw_input()

print("Enter the bits length : ")
num3 = raw_input()
num4 = num3

numbers = num1 + "," + num2 + "," + num3 + "," + num4

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost",5000))
clientsocket.send(numbers)
clientsocket.close()
