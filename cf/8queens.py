

import json
inf=open("8queens.json")
board=json.loads(inf.read())
board=board["matrix"]
for i in board:
	print(i)

def issafe(row,col):
	for i in range(8):
		for j in range(8):
			if(board[i][j]==1):
				if(row==i):
					return False
				if(col==j):
					return False
				if(abs(row-i)==abs(col-j)):
					return False
	return True

def place(col):
	if(col>=8):	
		print("\t\tCompleted...")
		return True
	for i in range(8):	
		if(issafe(i,col)):	
			board[i][col]=1 
			if(place(col+1)==True):	
				return True
			board[i][col]=0		
	return False


if(place(1)==True):
	print("solution found")
else:
	print("Solution not possible")
for i in board:
	print(i)








{"matrix": [

			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]}
