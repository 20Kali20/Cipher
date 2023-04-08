import random

alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
calf = alf.copy()
mess = input('Enter message: ')
cmess = []
key = {}

for x in alf:
    que = False
    while not que:
        clet = random.choice(calf)
        if clet != x:
            key[x] = clet
            calf.pop(calf.index(clet))
            que = True

for y in mess:
    cmess.append(key[y])

print(''.join(cmess))
print('Key: ')
for i in alf:
    print(i,' : ', key[i])