import psutil

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def test_hour():
    print(secs2hours(secs))

def giveMeBattery():
    battery = psutil.sensors_battery()
    return "charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft))

def test_battery():
    print(giveMeBattery())

def giveMePercentBattery():
    battery = psutil.sensors_battery()
    return battery.percent

def test_percentage():
    print(giveMePercentBattery())