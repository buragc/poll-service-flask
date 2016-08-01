from flask import Blueprint, jsonify, current_app, request
from .models import Poll, poll_schema, Vote
from . import db

main = Blueprint('app', __name__)


@main.route("/hello", methods=['GET'])
def hello():
    return jsonify({'msg': 'hello world'})


@main.route("/polls/<poll_id>", methods=['GET'])
def get_poll(poll_id):
    poll = Poll.query.filter_by(id=poll_id).first() or {}
    return jsonify(poll_schema.dump(poll).data)


@main.route("/polls/", methods=['POST'])
def create_poll():
    data, errors = poll_schema.load(request.json)
    if errors:
        return jsonify(jsonify(errors)), 422
    poll = data
    db.session.add(poll)
    db.session.commit()
    return jsonify({'id': poll.id})
