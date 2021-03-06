import wmi
import time
import math
import psutil
import subprocess
from tkinter import *
from tkinter import font
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pycaw import AudioUtilities, IAudioEndpointVolume
from threading import Timer
import os
import sys
import socket


def giveMeLoadAverage():
    p = psutil.Process()
    p_cpu_times = p.cpu_times()
    stat = p_cpu_times
    cpu_percent = p.cpu_percent(1)
    percent = cpu_percent, "%"
    return stat, percent


def giveMeIpV4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def giveMeIpPing():
    results = subprocess.check_output(["ping", "-n", "1", "localhost"])
    results = results.decode("ascii", "ignore")  
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[2]
    return ls

def giveMeRemainingSpace():
    mybytes = psutil.disk_usage('/').free / 1000000000
    return 'Free space on disk:', math.floor(mybytes), 'Go'

def giveMeTemperature():
    w = wmi.WMI(namespace="root\wmi")
    temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
    return str((temperature_info.CurrentTemperature-2732)/10.0), "celsius"

c = wmi.WMI ()
def giveMeWamp():
  for process in c.Win32_Service ():
        if process.Name == "wampapache64":
              if process.State == 'Stopped' :
                  return "offline"
              else :
                  return "online"

def giveMeDhcp():
    for process in c.Win32_Service ():
        if process.Name == "Dhcp" :
            if process.State == 'Stopped' :
                return "offline"
            else :
                return "online"


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

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def giveMeBattery():
    battery = psutil.sensors_battery()
    return "charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft))

def giveMePercentBattery():
    battery = psutil.sensors_battery()
    return battery.percent

def giveMeTime():
    return time.strftime("%A %d %B %Y %H:%M:%S")

def giveMeVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    getTheFuckinVolum = volume.GetMasterVolumeLevelScalar()
    getTheFuckinVolum = getTheFuckinVolum * 100
    return math.floor(getTheFuckinVolum)

def maj():
    # on arrive ici toutes les 1000 ms
    global Text2
    global Text3
    global Rect2
    global Percent1
    global Rect4
    global Percent2
    global Text5_2
    global Text4_3
    canvas.delete(Text3)
    canvas.delete(Text2)
    canvas.delete(Rect2)
    canvas.delete(Rect4)
    canvas.delete(Percent1)
    canvas.delete(Percent2)
    canvas.delete(Text5_2)
    canvas.delete(Text4_3)
    Text2 = canvas.create_text(1055, 165, text=giveMeTime(), font=orbiclean,fill = font_white)
    Text3 = canvas.create_text(1055, 315, text=giveMeBattery(), font=orbiclean, fill = font_white)
    random1 = 1035 + giveMePercentBattery()*1.6
    Rect2 = canvas.create_rectangle(1035, 10, random1, 35, fill="#00FF00") 
    Percent1 = canvas.create_text(1110, 20, text=str(giveMePercentBattery())+'%', font=orbiclean, fill='white')
    random2 = 590 - (giveMeVolume()) * 1.6
    Rect4 = canvas.create_rectangle(1155, random2, 1190, 590, fill="red")
    Percent2 = canvas.create_text(1173, 510, text=str(giveMeVolume()), font=orbiclean, fill='white')
    Text5_2 = canvas.create_text(170, 315, text=giveMeIpPing(), font=orbiclean, fill = font_white)
    Text4_3 = canvas.create_text(1040, 455, text=giveMeLoadAverage(), font=orbiclean, fill = font_white)
    fenetre.after(1000,maj)

def wampMaj():
    global Text7_2
    global Text8_2
    canvas.delete(Text7_2)
    canvas.delete(Text8_2)
    Text7_2 = canvas.create_text(105, 15, text=giveMeDhcp(), fill='red',  font=FatBigHyppo)
    Text8_2 = canvas.create_text(105, 35, text=giveMeWamp(), fill='red',  font=FatBigHyppo)

fenetre = Tk()
fenetre.title("l'Oeil de Xana")
# helv36 = tkFont.Font(family = "Helvetica",size = 36,weight = "bold") import tkFont

FatBigHyppo = font.Font(family='Orbitron', size=12, weight='bold')
orbiclean = font.Font(family='Orbitron', size=8)
font.families()

fenetre.resizable(width=False, height=False)
canvas = Canvas(fenetre, width=1200, height=600, background="#DBDBDB", cursor="arrow")
canvas.pack()
photo = PhotoImage(file="xana.png") # need resize
canvas.create_image(0, 0, anchor=NW, image=photo)
colorLines = "white"
colorLetters = "black"
font_white = "white"

white_line1 = canvas.create_line(0, 150, 200, 150, fill=colorLines)
white_line1_2 = canvas.create_line(200, 150, 200, 170, fill=colorLines)
Text1 = canvas.create_text(140, 140, text="Temperature", font=FatBigHyppo, fill = font_white )
Text1_2 = canvas.create_text(155, 165, text=giveMeTemperature(), font=orbiclean,fill = font_white)

white_line2 = canvas.create_line(950, 150, 1200, 150, fill=colorLines)
white_line2_2 = canvas.create_line(950, 150, 950, 170, fill=colorLines)
Text2_title = canvas.create_text(1020, 140, text='Date and Time', font=FatBigHyppo, fill = font_white)
Text2 = canvas.create_text(985, 165, text=giveMeTime(), font=orbiclean, fill = font_white)

white_line3 = canvas.create_line(950, 300, 1200, 300, fill=colorLines)
white_line3_2 = canvas.create_line(950, 300, 950, 320, fill=colorLines)
Text3_title = canvas.create_text(985, 290, text='Battery', font=FatBigHyppo, fill = font_white)
Text3 = canvas.create_text(985, 315, text=giveMeBattery(), font=orbiclean, fill = font_white)
Rect1 = canvas.create_rectangle(1035, 10, 1195, 35, fill=colorLetters)
random1 = 1035 + giveMePercentBattery()*1.6
Rect2 = canvas.create_rectangle(1035, 10, random1, 35, fill="#FD3F92")
Percent1 = canvas.create_text(1100, 20, text=str(giveMePercentBattery())+'%', font=orbiclean, fill='white')

white_line4 = canvas.create_line(950, 400, 1200, 400, fill=colorLines)
white_line4_2 = canvas.create_line(950, 400, 950, 420, fill=colorLines)
Text4_Title = canvas.create_text(975, 390, text="Disk", font=FatBigHyppo, fill = font_white)
Text4 = canvas.create_text(1040, 415, text=giveMeRemainingSpace(), font=orbiclean,fill = font_white)
Text4_2 = canvas.create_text(1000, 435, text="{use of the cpu => }", font=orbiclean, fill = font_white)
Text4_3 = canvas.create_text(1040, 455, text=giveMeLoadAverage(), font=orbiclean, fill = font_white)

Rect3 = canvas.create_rectangle(1155, 430, 1190, 590, fill=colorLetters)
random2 = 590 - (giveMeVolume()) * 1.6
Rect4 = canvas.create_rectangle(1155, random2, 1190, 590, fill="red")
Percent2 = canvas.create_text(1173, 510, text=str(giveMeVolume()), font=orbiclean, fill='white')

white_line5 = canvas.create_line(0, 300, 250, 300, fill=colorLines)
white_line5_2 = canvas.create_line(250, 300, 250, 320, fill=colorLines)
Text5 = canvas.create_text(215, 290, text="PING", font=FatBigHyppo)
Text5_2 = canvas.create_text(170, 315, text=giveMeIpPing(), font=orbiclean,fill = font_white)
Text5_3 = canvas.create_text(170, 335, text=giveMeIpV4(), font=orbiclean, fill = font_white)

white_line6 = canvas.create_line(0, 450, 300, 450, fill=colorLines)
white_line6_2 = canvas.create_line(300, 450, 300, 470, fill=colorLines)
Text6_Title = canvas.create_text(265, 440, text='Wifi', font=FatBigHyppo, fill = font_white)
Text6 = canvas.create_text(200, 460, text=giveMeWifi(), font=orbiclean, fill = font_white)

Text7 = canvas.create_text(40,  15, text="DHCP : ", font=FatBigHyppo, fill = font_white)
Text7_2 = canvas.create_text(100, 15, text="Loading...", fill='red', font=orbiclean)
Text8 = canvas.create_text(40, 35, text="WAMP : ", font=FatBigHyppo, fill = font_white)
Text8_2 = canvas.create_text(100, 35, text="Loading...", fill='red',  font=orbiclean)



maj()
#wampMaj()
fenetre.mainloop()
# changer la taille = font=("Purisa", 12)
# effet hober = activefill="red"
# changer curseur = cursor="pirate"