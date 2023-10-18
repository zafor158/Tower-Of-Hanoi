import view

model = [[1, 2,3],[],[]]


def hanoi(ndiscs, src, dest, aux):
    global model
    if ndiscs == 1 :
        print("move disc from %s to %s" % (src,dest))
        print(model)
        view.moveDisc(model,src,dest)
        model[dest].append(model[src].pop()) # move disc from src to dest
    else :
        hanoi(ndiscs-1, src, aux, dest)
        hanoi(1, src, dest, aux)
        hanoi(ndiscs-1, aux, dest, src)

ndiscs = 5
view.init(model)
hanoi(ndiscs, 0, 2, 1)

