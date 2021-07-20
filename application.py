from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import prisma.api.cartelist as ct
import json
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



api.add_resource(giveMission, '/mission/')
api.add_resource(giveMissionbyIndex, '/mission/index/<string:todo_id>')
api.add_resource(giveAllMission, '/mission/all/')

if __name__ == '__main__':
#    #app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    app.run()






