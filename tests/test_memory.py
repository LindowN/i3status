import psutil
import math

def giveMeRemainingSpace():
    mybytes = psutil.disk_usage('/').free / 1000000000
    return 'Free space on disk:', math.floor(mybytes), 'Go'

def test_answer():
    print(giveMeRemainingSpace());