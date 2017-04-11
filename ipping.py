'''
import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

print(get_ip_address())'''

import os
import sys

for i in range(10):
    os.system('ping -t localhost')
    print("finishing pinging the localhost - %d" % i)
    sys.stdout.flush()
