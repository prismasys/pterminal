from os import system, name

import time
import prisma.utils.push as push
import prisma.api.cartelist as cartelist
import prisma.utils.cartelutils as cutils


def cartelworker():

    print('PRISMA BOUNTY HUNTER SHERIFF\n')
    stop = 0
    subprocess = 0

    while stop == 0:
        print('\n')
        print('1 - To stop this environment\n')
        print('2 - To start sending cartels to subs\n')
        print('3 - To send a custom message\n')
        print('\n---------------------------\n')
        inpoot = int(input())

        if inpoot == 1:
            stop = 1
        elif inpoot == 2:

            auxcartel = []

            while subprocess == 0:

                x = cartelist.getmissionsdict()

                if auxcartel == x['cartel0']['title']:
                    print('Detected Same list')
                    time.sleep(60)
                    continue
                else:
                    auxcartel = x['cartel0']['title']

                    print(x['cartel0'])

                    for i in range(1):
                        cartelname = 'cartel{}'.format(i)
                        print(x[cartelname]['title'])
                        tit = x[cartelname]['title']
                        print(x[cartelname]['link'])
                        link = x[cartelname]['link']
                        push.carteltopusher2(tit, 'Click to apply', link)


        elif inpoot == 3:
            print('Enter message')
            msg = input()
            push.msgtopusher(msg)
            continue
        else:
            continue

def soloworker(min):

    secs = min*60

    print('PRISMA BOUNTY HUNTER SHERIFF\n')
    stop = 0
    auxcartel = []

    while stop == 0:

        x = cartelist.getmissionsdict()

        if auxcartel == x['cartel0']['title']:
            print('No more cartels! Waiting for more...\n')
            print('Checking in the next {} minute(s)...'.format(min))
            time.sleep(secs)
            continue
        else:
            print('I found a cartel!.\n')
            print('WANTED! Dead Or Alive.\n')
            auxcartel = x['cartel0']['title']

            for i in range(2):
                cartelname = 'cartel{}'.format(i)
                cartel = x[cartelname]

                ss = cutils.getshortsummary(cartel)

                hr = cutils.gethourlyrate(cartel)

                country = cutils.getcountry(cartel)

                print(x[cartelname]['title'])
                tit = x[cartelname]['title']
                print(x[cartelname]['link'])
                link = x[cartelname]['link']
                push.carteltopusher2(tit, 'Click to apply', link)
                print('Cartel Send!\n')


