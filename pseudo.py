import datetime
now = datetime.datetime.now()
seed = int(now.strftime("%Y%m%d%H%M%s"))
a = 1103515245
c = 12345
m = pow(2,32)
def LCG() :
    global seed
    seed = (a * seed + c) % m
    return seed
print("How many random numbers do you want ? ")
n = int(raw_input())
i = 0
while i<n :
    print(LCG())
    i = i + 1
