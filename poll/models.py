from . import db, ma
from utils import timestamp, uniqueid
from marshmallow import post_load


class Poll(db.Model):
    """Poll model"""
    __tablename__ = "polls"
    id = db.Column(db.String(36), primary_key=True, default=uniqueid)
    created_at = db.Column(db.Integer, default=timestamp)
    updated_at = db.Column(db.Integer, default=timestamp, onupdate=timestamp)
    question = db.Column(db.String(140))
    poll_opt0 = db.Column(db.String(40))
    poll_opt1 = db.Column(db.String(40))
    poll_opt2 = db.Column(db.String(40))
    votes = db.relationship('Vote', backref='poll', lazy='dynamic')

    @staticmethod
    def create():
        poll = Poll()
        return poll

class Vote(db.Model):
    """A vote representation for a given poll"""
    __tablename__ = "votes"
    id = db.Column(db.Integer, primary_key=True)
    useridentifier = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.Integer, default=timestamp)
    updated_at = db.Column(db.Integer, default=timestamp, onupdate=timestamp)
    poll_opt_index = db.Column(db.Integer, nullable=False)
    poll_id = db.Column(db.String(36), db.ForeignKey('polls.id'))


class PollSchema(ma.ModelSchema):
    class Meta:
        model = Poll


class VoteSchema(ma.ModelSchema):
    class Meta:
        model = Vote

poll_schema = PollSchema()
