import time

def giveMeTime():
    return time.strftime("%A %d %B %Y %H:%M:%S")

def test_date():
    print(giveMeTime)