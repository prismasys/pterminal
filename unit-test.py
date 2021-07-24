import time

import prisma.utils.push as push
import prisma.api.cartelist as cartelist

import requests

json_comp = {
            'cartel': {
                'title': 'Fulestac nided',
                'subtitle': 'In oklajoma',
                'url': 'www.www.com'
            }
        }

jsonstr = "json_comp = {'cartel': {'title': 'Fulestac nided','subtitle': 'In oklajoma','url': 'www.www.com'}}"

url = 'http://127.0.0.1:5000/carteltosubs/{}'.format(jsonstr)

r = requests.get(url)



