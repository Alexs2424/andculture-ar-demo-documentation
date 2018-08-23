from flask import Flask
from flask import Flask, request, render_template
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

## Documentation of ARObject class
#name - name of the object that you're looking for. (Superficial for now)
#objectType - what type of object you are going to manipulate (i.e. 2D Model, 3D Model, Plane)
#behaviour - what you are going to do to the object
#specifics - what specifically you are going to manipulate the object. (this might be changed later)
#specific_data - the number/data you need to manipulate the object in the way you would like.


#UPDATE THIS MODEL 
#BECAUSE THIS IS OUTDATED AND DOESN'T CONTAIN ALL OF THE DATA WE NEED
arObjects = [
    {
        "name" : "magazine",
        "objectType" : "2D Model",
        "behaviour" : "move",
        "specifics" : "Z",
        "specific_data" : 0.3
    },
    {
        "name" : "preview",
        "objectType" : "2D Model",
        "behaviour" : "move",
        "specifics" : "Z",
        "specific_data" : 0.67
    }
]

class ARObject(Resource):
    def get (self, name):
        for arObj in arObjects:
            if (name == arObj["name"]):
                return arObj, 200
        return "object not found", 404

    def post (self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("objectType")
        parser.add_argument("behaviour")
        parser.add_argument("specifics")
        parser.add_argument("specific_data")
        args = parser.parse_args()

        for arObj in arObjects:
            if (name == arObj["name"]):
                return "Object with name {} already exists".format(name), 400

        arObject = {
            "name" : name,
            "objectType" : args["objectType"],
            "behaviour" : args["behaviour"],
            "specifics" : args["specifics"],
            "specific_data" : args["specific_data"]
        }
        arObjects.append(arObject)
        return arObject, 201

    def put (self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("objectType")
        parser.add_argument("behaviour")
        parser.add_argument("specifics")
        parser.add_argument("specific_data")
        args = parser.parse_args()

        for arObj in arObjects:
            if (name == arObj["name"]):
                arObj["objectType"] = args["objectType"]
                arObj["behaviour"] = args["behaviour"]
                arObj["specifics"] = args["specifics"]
                arObj["specific_data"] = args["specific_data"]
                return arObj, 200

        arObject = {
            "name" : name,
            "objectType" : args["objectType"],
            "behaviour" : args["behaviour"],
            "specifics" : args["specifics"],
            "specific_data" : args["specific_data"]
        }
        arObjects.append(arObject)
        return arObject, 201

    def delete (self, name):
        global arObjects
        arObjects = [arObj for arObj in arObjects if arObj["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(ARObject, "/arObj/<string:name>")

#Home endpoint for the Api
@app.route('/')
def root(): #uses the templates folder so that we can render a custom page
    return render_template('ARImageDatabaseAPI.html')
    #return 'Welcome to the ar database testing website.' returns the string that is rendered into html on the page


app.run(debug=True)
