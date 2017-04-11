import subprocess

def giveMeWifi():
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii", "ignore")  
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    f = open( 'conf.txt', 'w' )
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
            f.write( ls[x] + '\n' )
        x += 1
    f.close()
    return ssids[0]

def test_wifi():
    print(giveMeWifi())