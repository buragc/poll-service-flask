from . import db
from utils import timestamp, uniqueid


class Poll(db.Model):
    """Poll model"""
    __tablename__ = "poll"
    id = db.Column(db.String(36), primary_key=True, default=uniqueid())
    created_at = db.Column(db.Integer, default=timestamp)
    updated_at = db.Column(db.Integer, default=timestamp, onupdate=timestamp)
    poll_opt0 = db.Column(db.String(40))
    poll_opt1 = db.Column(db.String(40))
    poll_opt2 = db.Column(db.String(40))
    answers = db.relationship('Answers', backref='poll', lazy='dynamic')

    @staticmethod
    def create():
        poll = Poll()
        return poll


class Vote(db.Model):
    """A vote representation for a given poll"""
    __tablename__ = "vote"
    id = db.Column(db.Integer, primary_key=True)
    useridentifier = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.Integer, default=timestamp)
    updated_at = db.Column(db.Integer, default=timestamp, onupdate=timestamp)
    poll_opt_index = db.Column(db.Integer, nullable=False)
    poll_id = db.Column(db.String(36), db.ForeignKey('poll.id'))

