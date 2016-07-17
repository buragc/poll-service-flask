import os
import subprocess
import sys

from flask_script import Manager

from poll import create_app, db

manager = Manager(create_app)


@manager.command
def lint():
    """Run the code linter"""
    lintr = subprocess.call(['flake8', '--ignore=E402', 'poll', 'manage.py', 'tests/']) == 0
    if lintr:
        print("OK")
    sys.exit(lintr)


@manager.command
def createdb(drop_first=False):
    if drop_first:
        db.drop_all()
    db.create_all()


@manager.command
def test():
    """Runs unit tests in the code"""
    tests = subprocess.call(['python','-m', 'pytest','--cov=poll', 'tests/'])
    sys.exit(tests)


if __name__ == "__main__":
    if sys.argv[1] == 'test' or sys.argv[1] == 'lint':
        os.environ['POLLSVC_CONFIG'] = 'testing'
    manager.run()
