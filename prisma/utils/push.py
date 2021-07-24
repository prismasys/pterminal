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


def carteltopusher(title, subtitle, link):

    qlink = link.replace('//','totona')
    alink = qlink.replace('/', 'vagina')
    klink = alink.replace(':','clitoris')
    plink = klink.replace('.', 'pezon')

    json_comp = {
        'cartel': {
            'title': title,
            'subtitle': subtitle,
            'url': plink
        }
    }

    jco = {
    "cartel": {
        "title": title,
        "subtitle": subtitle,
      "url": plink
    }
}

    url = 'http://127.0.0.1:5000/carteltosubs'

    r = requests.get(url, json=jco)

    print(r.text)

    return True


def msgtopusher(msg):

    url = 'https://prismaterminal.herokuapp.com/msgtosubs/{}'.format(msg)

    r = requests.get(url)

    return True

def carteltopusher2(title, subtitle, link):

    qlink = link.replace('//', 'totona')
    alink = qlink.replace('/', 'vagina')
    klink = alink.replace(':', 'clitoris')
    plink = klink.replace('.', 'pezon')
    tlink = plink.replace('?', 'labia')

    json_comp = {
        'cartel': {
            'title': title,
            'subtitle': subtitle,
            'url': tlink
        }
    }

    jco = {
    "cartel": {
        "title": title,
        "subtitle": subtitle,
      "url": tlink
    }
}

    pushurl = 'https://prismaterminal.herokuapp.com/carteltosubs/%'

    strjco = json.dumps(jco)

    print(jco['cartel']['url'])

    print(strjco)

    purl = pushurl.replace('%', strjco)

    r = requests.get(purl)

    print('Notification Pushed!')

    return True