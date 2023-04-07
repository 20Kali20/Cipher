alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

mess = input('Enter message: ')
s = int(input('Enter key: '))
cmess = []

for x in range(len(mess)):
    i = alf.index(mess[x])
    if i + s > len(alf):
        cmess.append(alf[i + s - len(alf)])
    else:
        cmess.append(alf[i + s])
print(''.join(cmess))