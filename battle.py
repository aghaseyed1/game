li1 = [[100,10],[30,20]]
li2 = [[100,10],[20,20]]


def sim(x,y,typ=1):
    n = 1.5 #TODO: taviz bara tedad bala
    x1 = 0 #TODO: emtiyaz hojomi
    for i in x:
        x1 += i[0] * i[1]
    y1 = 0 #TODO: emtiyaz defai
    for i in y:
        y1 += i[0] * i[1]

    #tain barande va darsad koshte ha
    if x1 > y1:
        xwin = True
        alpha = y1/x1
    else:
        xwin = False
        alpha = x1/y1
    zarib = alpha ** n
    print(zarib)
    is_zarib_loser=0
    if typ==2: #raid
        zarib = zarib/(1+zarib)
        zarib_loser = 1-zarib
    #list jadid ke koshte ha ro neshon mide
    x2 = []
    y2 = []
    if xwin:
        for i in x:
            x2.append([i[0] * zarib ,i[1]])
        for i in y:
            if typ==2:
                y2.append([i[0] * zarib_loser ,i[1]])
            else:
                y2.append([0 ,i[1]])
    else:
        for i in y:
            y2.append([i[0] * zarib ,i[1]])
        for i in x:
            if typ==2:
                x2.append([i[0] * zarib_loser ,i[1]])
            else:
                x2.append([0 ,i[1]])
    return x2,y2
print(sim(li1,li2,2))
