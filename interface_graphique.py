from tkinter import *
from tkinter import font
import time
import psutil

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def giveMeBattery():
    battery = psutil.sensors_battery()
    battery
    return "charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft))

def giveMeTime():
    return time.strftime("%A %d %B %Y %H:%M:%S")

def maj():
    # on arrive ici toutes les 1000 ms
    global Text2
    global Text3
    canvas.delete(Text3)
    canvas.delete(Text2)
    Text2 = canvas.create_text(1083, 165, text=giveMeTime())
    Text3 = canvas.create_text(985, 290, text=giveMeBattery())
    fenetre.after(1000,maj)

fenetre = Tk()
fenetre.title("i3Status")
# helv36 = tkFont.Font(family = "Helvetica",size = 36,weight = "bold") import tkFont

tahoma = font.Font(family='Obytron', size=12, weight='bold')
cancer = font.Font(family='Purisa', size=12, weight='bold')
font.families()

fenetre.resizable(width=False, height=False)
canvas = Canvas(fenetre, width=1200, height=600, background="#5A5E6B", cursor="pirate")
canvas.pack()

white_line1 = canvas.create_line(0, 150, 200, 150, fill="white")
white_line1_2 = canvas.create_line(200, 150, 200, 170, fill="white")
Text1 = canvas.create_text(165, 140, text="SOMETHING")

white_line2 = canvas.create_line(1000, 150, 1200, 150, fill="white")
white_line2_2 = canvas.create_line(1000, 150, 1000, 170, fill="white")
Text2_title = canvas.create_text(1055, 140, text='Date and Time', font=tahoma)
Text2 = canvas.create_text(1083, 165, text=giveMeTime())

white_line3 = canvas.create_line(950, 300, 1200, 300, fill="white")
white_line3_2 = canvas.create_line(950, 300, 950, 320, fill="white")
Text3 = canvas.create_text(985, 290, text=giveMeBattery(), font=cancer)

white_line4 = canvas.create_line(900, 450, 1200, 450, activefill="red", fill="white")
white_line4_2 = canvas.create_line(900, 450, 900, 470, fill="white")
Text4 = canvas.create_text(935, 440, activefill="red", text="SOMETHING")

white_line5 = canvas.create_line(0, 300, 250, 300, fill="white")
white_line5_2 = canvas.create_line(250, 300, 250, 320, fill="white")
Text5 = canvas.create_text(215, 290, text="SOMETHING")

white_line6 = canvas.create_line(0, 450, 300, 450, fill="white")
white_line6_2 = canvas.create_line(300, 450, 300, 470, fill="white")
Text6 = canvas.create_text(265, 440, text="SOMETHING")


#photo = PhotoImage(file="url") # need resize
#canvas.create_image(200, 0, anchor=NW, image=photo)


maj()
fenetre.mainloop()


# changer la taille = font=("Purisa", 12)
# effet hober = activefill="red"
# changer curseur = cursor="pirate"