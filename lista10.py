# 1
t1 = (2, 5, 'piesek', 7.89)
t2 = (6, 8, 'kot', 0.14)
t = t1 + t2
print(t)
t1 *= 2
t2 *= 2
print(t1)
print(t2)
print(len(t1))
print(len(t2))
t1 = (2, 5, 7.89)
t2 = ('test', 'mniejszy', 'wyższy')
print(max(t1))
print(max(t2))
l = list(t1)
del(t1)
l[1] = 'zmiana'
t1 = tuple(l)
print(t1)

print('\n')
# 2
sl = {'Imie': 'Anna', 'Wiek': 30, 5: 'Costam', (6, 2): 32}
sl['dodatki'] = 'Costam'
print(sl.keys())
print(sl.values())
print(sl)
del sl['Wiek']
l1 = [56, 'test', 4.5, 'G', 20]
l2 = [65, 'start', 4.0, 'H', 30]
dict = {}
for i in range(0,5):
    dict[l1[i]] = l2[i]
print('\n', dict)

print('\n')
# 3
def bezpowt(sl):
    vallist = list(sl.values())
    for i in range(0, len(vallist)):
        check = vallist[i]
        for j in range(i + 1, len(vallist)):
            if check == vallist[j]:
                return 0
    return 1
sl1 = {'id': 67, 'wiek': 47, 7: 67}
sl2 = {'id': 67, 'wiek': 57, 7: 29}
answer = bezpowt(sl1)
print(answer)
answer = bezpowt(sl2)
print(answer)

print('\n')
# 4
def bezpowt(sl):
    vallist = list(sl.values())
    for i in range(0, len(vallist)):
        check = vallist[i]
        for j in range(i + 1, len(vallist)):
            if check == vallist[j]:
                return 0
    return 1


def odwr(sl):
    if bezpowt(sl) != 0:
        sl2 = {}
        keys = list(sl.keys())
        values = list(sl.values())
        for i in range(0, len(values)):
            sl2[values[i]] = keys[i]
        return sl2
    else:
        print('Error! Values not unique!')


sl1 = {'latać': 'fly', 'samolot': 'plane', 'wiek': 'age', 'zamek': 'castle'}
print(sl1)
sldrugi = {'latać': 'fly', 'samolot': 'plane', 'wiek': 'age', 'zamek': 'age'}
sl2 = odwr(sl1)
print(sl2)
sl2 = odwr(sldrugi)

print('\n')
# 5
sl = {'latać': 'fly', 'samolot': 'plane', 'wiek': 'age', 'zamek': 'castle'}
fo = open('plik.txt', 'w')
lkey = list(sl.keys())
lvalue = list(sl.values())
for i in range(0, len(lvalue)):
    fo.write(lkey[i])
    fo.write(':')
    fo.write(lvalue[i])
    fo.write(';')
fo.close()

print('\n')
# 6
fo = open('plik.txt', 'r')
keys = []
values = []
chain = fo.read()
fo.close()
chain = chain.split(';')
chain.remove('')
all  = []
for i in range(0, len(chain)):
    all += (chain[i].split(':'))
for i in range(0, len(all)):
    if i % 2 == 0:
        keys.append(all[i])
    else:
        values.append(all[i])
sl = {}
for i in range(0, len(values)):
    sl[keys[i]] = values[i]
print(sl)