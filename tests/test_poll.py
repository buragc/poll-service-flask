from poll import create_app
from flask import jsonify, url_for, json
import pytest
from poll import db as _db


@pytest.fixture
def app():
    app = create_app('testing')
    return app


def testHello(client):
    result = client.get(url_for('app.hello')).json
    print("Result is:\n")
    assert (result['msg'] == 'hello world')


def testCreatePoll(client):
    result = client.post(url_for('app.create_poll')).json
    print(result['id'])
    assert (result['id'] != "")


def testSilly():
    assert ("12345" == "12345")


