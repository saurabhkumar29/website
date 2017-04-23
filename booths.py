from bitstring import BitArray

def booth(m, r, x, y):

	totalLength = x + y + 1
	A = BitArray(int = m, length = totalLength) << (y+1)
	S = BitArray(int = -m, length = totalLength)  << (y+1)
	P = BitArray(int = r, length = y)
	P.prepend(BitArray(int = 0, length = x))
	P = P << 1
	print "Initial values"
	print "A", A.bin
	print "S", S.bin
	print "P", P.bin
	print "Starting calculation"
	for i in range(1,y+1):
		if P[-2:] == '0b01':
			P = BitArray(int = P.int + A.int, length = totalLength)
			print "P +  A:", P.bin
		elif P[-2:] == '0b10':
			P = BitArray(int = P.int +S.int, length = totalLength)
			print "P +  S:", P.bin
		P = arith_shift_right(P, 1)
		print "P >> 1:", P.bin
	P = arith_shift_right(P, 1)
	print "P >> 1:", P.bin
	return P.int

def arith_shift_right(num, bits):
    l = num.len
    num = BitArray(int = (num.int >> bits), length = l)
    return num

if __name__ == "__main__":
        print booth(4, 3, 10, 10)
