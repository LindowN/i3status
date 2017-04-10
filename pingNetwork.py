import os

def check_ping():

    hostname = "8.8.8.8"
    response = os.system("ping -t 1" + hostname)
#response = os.system("ping -n 1" + hostname)
    if response == 0:
        ping_status = hostname + " is up"
    else:
        ping_status = hostname + " is down"

    return ping_status

ping = check_ping()
print(ping)

