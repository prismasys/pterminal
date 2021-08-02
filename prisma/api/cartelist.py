from prisma.api.core import mission
from prisma.api import feed

def getmissions():

    feeds = feed.upworkfeed()

    cartels = []

    cartelsdict = {}

    for i in range(len(feeds.entries)):
        miss = mission(feeds.entries[i])
        cartels.append(miss)
        cartelv = 'cartel{}'.format(i)
        cartelsdict[cartelv] = miss.entry

    return cartels

def getmissionsdictv1():

    feeds = feed.upworkfeedv1()

    cartels = []

    cartelsdict = {}

    for i in range(len(feeds.entries)):
        miss = mission(feeds.entries[i])
        cartels.append(miss)
        cartelv = 'cartel{}'.format(i)
        cartelsdict[cartelv] = miss.entry

    return cartelsdict

def getmissionsdict():

    feeds = feed.upworkfeed()

    cartels = []

    cartelsdict = {}

    aux = 0

    for items in feeds:
        for i in range(len(items.entries)):
            miss = mission(items.entries[i])
            cartels.append(miss)
            aux = aux + 1
            cartelv = 'cartel{}'.format(aux)
            cartelsdict[cartelv] = miss.entry


    return cartelsdict