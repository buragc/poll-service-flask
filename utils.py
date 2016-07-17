import time
import uuid


def timestamp():
    """Return current time as int"""
    return int(time.time())


def uniqueid():
    """Return a unique id as string"""
    return str(uuid.uuid4())
