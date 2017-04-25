import random
def numberOfBits(p):
    return (len(bin(p))-2)

def brutalPrime(n) :
    for i in range(2,n/2):
        if n % i == 0 :
            return False
    return True

def pseudoPrimeMillerRabin(n) :
    for i in range(0,1000) :
        randomCheck = random.randint(2,(n-2))
        if (n % randomCheck) == 0 :
            return False
    return True

print("\nEnter the parameter tuple (p,q,g) : ")
a=input()
b=input()
p = long(pow(a,b))
print("\np: "+str(p))

a=input()
b=input()
q = long(pow(a,b))
print("\nq: "+str(q))

g = long(raw_input())

print("Here's how good the DSA tuple is -> ")
print("According to brute-force primality testing is q prime ?")
print(brutalPrime(q))

print("According to Miller-Rabin primality testing, q is most probably prime ?")
print(pseudoPrimeMillerRabin(q))
Qbits = numberOfBits(q)
print("Is number of bits of q = 160 ?")
print(Qbits == 160)
print("Does q divide (p-1) ?")
print(((p-1) % q) == 0)

print("Is number of bits of p between 512 & 1024 ? ")
Pbits = numberOfBits(p)
print((Pbits >= 512) and (Pbits <= 1024))
print("Is g of the right form i.e. (h^((p-1)/q) mod p) where h = 2 ?")
h = 2
complexExponent = ((p-1) / q)
print((pow(h,complexExponent) % p) == g)
