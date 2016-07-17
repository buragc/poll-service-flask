from flask import Blueprint, jsonify, current_app
from .models import Poll, Vote
from . import db

main = Blueprint('app', __name__)


@main.route("/hello", methods=['GET'])
def hello():
    return jsonify({'msg': 'hello world'})


@main.route("/polls/<id>", methods=['GET'])
def get_poll(id):
    return jsonify(Poll.create())


@main.route("/polls/", methods=['POST'])
def create_poll():
    poll = Poll.create()
    db.session.add(poll)
    db.session.commit()
    return jsonify({'id': poll.id})