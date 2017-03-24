import os

print(os.getloadavg())

toto = os.times().user
#(1.296875, 0.765625, 0.0, 0.0, 0.0)
print(toto)
#times() -> (utime, stime, cutime, cstime, elapsed_time)

#Return a tuple of floating point numbers indicating process times.