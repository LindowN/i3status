import os

def check_ping():

    hostname = "google.com"
    response = os.system("ping -t 1" + hostname)

    if response == 0:
        ping_status = hostname + " is up"
    else:
        ping_status = hostname + " is down"

    return ping_status

ping = check_ping()
print(ping)