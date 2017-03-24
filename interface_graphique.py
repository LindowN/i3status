from tkinter import * 

fenetre = Tk()
fenetre.resizable(width=False, height=False)
canvas = Canvas(fenetre, width=1200, height=600, background="#5A5E6B")

white_line1 = canvas.create_line(0, 150, 200, 150, fill="white")
white_line1_2 = canvas.create_line(200, 150, 200, 170, fill="white")
Text1 = canvas.create_text(165, 140, text="SOMETHING")

white_line2 = canvas.create_line(1000, 150, 1200, 150, fill="white")
white_line2_2 = canvas.create_line(1000, 150, 1000, 170, fill="white")
Text2 = canvas.create_text(1035, 140, text="SOMETHING")

white_line3 = canvas.create_line(950, 300, 1200, 300, fill="white")
white_line3_2 = canvas.create_line(950, 300, 950, 320, fill="white")
Text3 = canvas.create_text(985, 290, text="SOMETHING")

white_line4 = canvas.create_line(900, 450, 1200, 450, fill="white")
white_line4_2 = canvas.create_line(900, 450, 900, 470, fill="white")
Text4 = canvas.create_text(935, 440, text="SOMETHING")

white_line5 = canvas.create_line(0, 300, 250, 300, fill="white")
white_line5_2 = canvas.create_line(250, 300, 250, 320, fill="white")
Text5 = canvas.create_text(215, 290, text="SOMETHING")

white_line6 = canvas.create_line(0, 450, 300, 450, fill="white")
white_line6_2 = canvas.create_line(300, 450, 300, 470, fill="white")
Text6 = canvas.create_text(265, 440, text="SOMETHING")

#photo = PhotoImage(file="url") # need resize
#canvas.create_image(200, 0, anchor=NW, image=photo)

canvas.pack()

fenetre.mainloop()