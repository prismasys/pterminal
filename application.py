from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import prisma.api.cartelist as ct
import prisma.utils.push as push
import prisma.utils.worker as worker
import json
import requests
import os


app = Flask(__name__)
api = Api(app)
CORS(app)

class giveMission(Resource):

    def get(self):

        misslist = ct.getmissions()

        miss = misslist[0]

        print(miss.entry)

        return miss.entry

class giveMissionbyIndex(Resource):

    def get(self, todo_id):

        print(todo_id)

        x = json.loads(todo_id)

        print(x['index'])

        misslist = ct.getmissions()

        miss = misslist[int(x['index'])]

        print(miss.entry)

        return miss.entry

class giveAllMission(Resource):

    def get(self):

        misslist = ct.getmissionsdict()


        return misslist

class SubscribePush(Resource):

    def get(self, todo_id):

        raw = todo_id.replace('totona','https://fcm.googleapis.com/fcm/send/')

        sub = json.loads(raw)

        push.subscribe(sub)

        push.pushnotif(sub)

        return 'Yay'


class MessagetoSubs(Resource):

    def get(self, todo_id):
        print(todo_id)

        # push.msgtosubs('Prisma Devs',todo_id)



        return 'Message Sended'

class CarteltoSubs(Resource):

    def get(self, todo_id):

        print(todo_id)

        litecartel = json.loads(todo_id)

        push.msgtosubs('Prisma Devs', litecartel['cartel']['title'])

        return 'Cartel Sended'

api.add_resource(giveMission, '/mission/')
api.add_resource(giveMissionbyIndex, '/mission/index/<string:todo_id>')
api.add_resource(SubscribePush, '/push/<string:todo_id>')
api.add_resource(MessagetoSubs, '/msgtosubs/<string:todo_id>')
api.add_resource(CarteltoSubs, '/carteltosubs/<string:todo_id>')


if __name__ == '__main__':
#    #app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    app.run()




