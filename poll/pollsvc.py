from flask import Blueprint, jsonify, current_app
from .models import Poll, Vote

main = Blueprint('app', __name__)


@main.route("/hello", methods=['GET'])
def hello():
    return jsonify({'msg': 'hello world'})


@main.route("/polls/<id>", methods=['GET'])
def get_poll(id):
    return jsonify(Poll.create())