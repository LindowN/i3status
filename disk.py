import psutil
import math

mybytes = psutil.disk_usage('/').free / 1000000000
print('Free space on disk:', math.floor(mybytes), 'Go')
