import time

import prisma.utils.push as push
import prisma.api.cartelist as cartelist
import prisma.utils.worker as worker

def gethourlyrate(cartel):

    s = cartel['summary']

    index = s.find("Hourly Range")

    hourlydiv = s[index:index + 31]

    index2 = hourlydiv.find(':')

    hr = hourlydiv[index2 + 2:index2 + 15]

    hr2 = hr.replace('$','US')

    return hr2


def getshortsummary(cartel):
    s = cartel['summary']

    shortsum = s[0:70]

    nss = shortsum.replace('<br', '')

    mss = nss.replace('/>', '')

    short = mss + '...'

    return short


def getcountry(cartel):

    s = cartel['summary']

    index = s.find('<b>Country</b>:')


    country = s[index + 16:index + 30]

    ncountry = country.replace('<br', '')

    mcountry = ncountry.replace('/>','')

    return mcountry

def muchotesto(cartel):

    s = cartel['summary']

    cantidaddetesto = len(s)

    print(cantidaddetesto)

    if cantidaddetesto > 600:
        print('Mucho testo')
        return True
    else:
        print('Cantidad adecuada de testo')
        return False

