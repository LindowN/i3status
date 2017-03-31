import psutil,os

'''cpu_times = psutil.cpu_times()
print(cpu_times)
cpu_percent = psutil.cpu_percent()
print(cpu_percent)'''
p = psutil.Process()
p_cpu_times = p.cpu_times()
print(p_cpu_times)
cpu_percent = p.cpu_percent(1)
print(cpu_percent)
