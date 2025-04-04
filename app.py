from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item, 200
        return {"message": "Item not found"}, 404

    def post(self, name):
        data = request.get_json()
        new_item = {"name": name, "price": data["price"]}
        items.append(new_item)
        return new_item, 201

    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {"message": "Item deleted"}, 200

api.add_resource(Item, "/item/<string:name>")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
