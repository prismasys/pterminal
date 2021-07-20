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

def getmissionsdict():

    feeds = feed.upworkfeed()

    cartels = []

    cartelsdict = {}

    for i in range(len(feeds.entries)):
        miss = mission(feeds.entries[i])
        cartels.append(miss)
        cartelv = 'cartel{}'.format(i)
        cartelsdict[cartelv] = miss.entry

    return cartelsdict