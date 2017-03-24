import psutil
import math

free_space = psutil.disk_usage('/').free / 8 * (10 ** -9)
print('Free space on disk:', math.floor(free_space), 'Go')

print(psutil.net_if_addrs().broadcast)