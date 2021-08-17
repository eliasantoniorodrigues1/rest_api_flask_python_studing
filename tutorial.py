from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

names = {
    "elias": {"age": 34, "sex": "male"},
    "Quedma": {"age": 29, "sex": "female"}
}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == '__main__':
    # Minha api vai fazer um get ou um post?
    # Poso fazer os dois, um get e um post
    app.run(debug=True)
