import json
import os
import requests


def subscribe(subscription):
    print(subscription)
    print(subscription['keys']['p256dh'])
    subtitle = 'prisma/assets/{}.json'.format(subscription['keys']['p256dh'])
    with open(subtitle, 'w', encoding='utf-8') as f:
        json.dump(subscription, f, ensure_ascii=False, indent=4)

    print('Sub saved to ', subtitle)
    return True

def load_subscribers():

    arr = os.listdir('prisma/assets')

    sublist = []

    for subdoc in arr:

        with open('prisma/assets/{fname}'.format(fname=subdoc)) as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()

        sublist.append(jsonObject)
    return sublist

def pushnotif(sub):

    json_comp = {
        'pushit': {
            'sub': sub,
            'title': 'Prisma Bounty Hunter',
            'subtitle': 'Yeeeeeeehaaaaw get ready for the rodeo',
            'url': 'https://prismasys.site/'
        }
    }



    pushurl = 'https://bhpush.herokuapp.com/subscribedev'

    r = requests.post(pushurl, json=json_comp)

    print('Notification Pushed!')


def msgtosubs(title, subtitle):

    sublist = load_subscribers()

    for sub in sublist:
        json_comp = {
            'pushit': {
                'sub': sub,
                'title': title,
                'subtitle': subtitle,
                'url': 'https://prismasys.site/'
            }
        }

        pushurl = 'https://bhpush.herokuapp.com/subscribedev'

        r = requests.post(pushurl, json=json_comp)

        print('Notification Pushed!')


def carteltosubs(title, subtitle, url):

    sublist = load_subscribers()

    for sub in sublist:
        json_comp = {
            'pushit': {
                'sub': sub,
                'title': title,
                'subtitle': subtitle,
                'url': url
            }
        }

        pushurl = 'https://bhpush.herokuapp.com/subscribedev'

        r = requests.post(pushurl, json=json_comp)

        print('Notification Pushed!')


