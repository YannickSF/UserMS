
from flask import Flask, request
from flask_cors import CORS
from app.domain import Domain

app = Flask(__name__)
cors = CORS(app)

ctx = Domain()


@app.route("/")
def index():
    # validate origin.
    return {'status': 200}


@app.route("/users", methods=['POST'])
def post_user():
    if request.method == 'POST':
        return {'response': ctx.create_user(**request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/users", methods=['GET'])
def get_users():
    if request.method == 'GET':
        return {'response': ctx.read_user()}

    return {'error': 'method not allow.'}


@app.route("/users/<string:id>", methods=['GET'])
def get_user_by_id(id):
    if request.method == 'GET':
        return {'response': ctx.read_user_by_id(id)}

    return {'error': 'method not allow.'}


@app.route("/users/<string:id>", methods=['PUT'])
def put_user(id):
    if request.method == 'PUT':
        return {'response': ctx.update_user(id, **request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/users/<string:id>", methods=['DELETE'])
def delete_user(id):
    if request.method == 'DELETE':
        return {'response': ctx.delete_user(id)}

    return {'error': 'method not allow.'}
