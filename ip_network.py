'''from __future__ import print_function
import socket

import psutil


af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
}

duplex_map = {
    psutil.NIC_DUPLEX_FULL: "full",
    psutil.NIC_DUPLEX_HALF: "half",
    psutil.NIC_DUPLEX_UNKNOWN: "?",
}


def main():
    stats = psutil.net_if_stats()
    io_counters = psutil.net_io_counters(pernic=True)
    for nic, addrs in psutil.net_if_addrs().items():
        print("%s:" % (nic))
        for addr in addrs:
            print("    %-4s" % af_map.get(addr.family, addr.family), end="")
            print(" address   : %s" % addr.address)
            if addr.broadcast:
                print("         broadcast : %s" % addr.broadcast)
            if addr.netmask:
                print("         netmask   : %s" % addr.netmask)
            if addr.ptp:
                print("      p2p       : %s" % addr.ptp)
        print("")


if __name__ == '__main__':
    main()'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()