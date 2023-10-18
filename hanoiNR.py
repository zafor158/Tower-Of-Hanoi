#  hanoiNR.py  - non recursive
#
model = [[1, 2, 3, 4], [], []]


def move1(src, dest):
    print("move disk from %s to %s" % (src, dest))
    model[dest].append(model[src].pop())


def move2(src, dest, aux) :
    move1(src, aux)
    move1(src, dest)
    move1(aux, dest)


def move3(src, dest, aux) :
    move2(src,aux,  dest)
    move1(src,dest)
    move2(aux,dest, src)


def move4(src, dest, aux):
    move3(src, aux,  dest)
    move1(src, dest)
    move3(aux, dest, src)


print(model)
move4(0, 1, 2)
print(model)

