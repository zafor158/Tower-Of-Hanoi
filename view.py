#  view.py
#
from graphics import *
win = GraphWin("Tower of Hanoi", 400, 400)

discAttr = {1:(60,"red"), 2:(50,'orange'), 3:(40,'yellow'), 4:(30,'green'), 5:(20, 'white')}
pegAttr = (('A',100), ('B',200), ('C',300))
discRects = {}


def drawPoles():
    for tag, xpos in pegAttr :
        makeRect("black", xpos, 200, 10, 100).draw(win)


def drawDiscs(peg, discs) :
    ndiscs = len(discs)
    for i in range(ndiscs) :
        drawDisc(peg, i, discs[i])


def drawDisc(peg, ndiscs,disc) :
    tag, pegPos = pegAttr[peg]
    top = pegTop(ndiscs)
    width,color = discAttr[disc]
    rect = makeRect(color, pegPos, top, width, 10).draw(win)
    discRects[disc] = rect


def makeRect(color, x,y, width,height) :  # x=center, y=bottom
    half = width//2
    c1 = Point(x-half, y)
    c2 = Point(x+half, y-height)
    rect = Rectangle(c1, c2)
    rect.setFill(color); rect.setWidth(0)
    return rect


def calcPath(model, start, stop) :     # peg-start (0-2) to peg-stop (0-2)
    disc = model[start][-1]
    xdist = pegAttr[stop][1]-pegAttr[start][1]
    xsteps= abs(xdist);  xinc=xdist/xsteps
    yup  = pegTop(len(model[start] ))-80
    ydown= pegTop(len(model[stop])+1)-80  # plus space not there yet

    return disc, ((yup,0,-1), (xsteps,xinc,0), (ydown,0,1))


def pegTop(ndiscs) :      # return open position x,y
    return 200 - ndiscs*11


def moveDisc(model, start, stop) :
    disc, path = calcPath(model, start, stop)
    rect = discRects[disc]
    moveRect(rect, path)


def moveRect(rect, amounts) :
    for steps,dx,dy in amounts :
        for i in range(steps) :
            rect.move(dx,dy)
            time.sleep(.01)


def init(model) :
    drawPoles()
    for peg in range(len(model)) :
        discs = model[peg]
        drawDiscs(peg, discs)


def test() :
    model = [[1],[],[]]
    model = [[1,2],[3],[4]]
    init(model)
    
    pegA = input("From peg (0,1,2):")
    pegB = input("To   peg (0,1,2):")
    moveDisc(model, int(pegA), int(pegB))


if __name__ == "__main__" : test()
