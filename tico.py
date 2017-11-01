from Tkinter import *  #often people import Tkinter as *
root = Tk()
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.grid()
check = canvas.create_line(200, 0,200, 600, fill='red', width=20)
line = canvas.create_line(400, 0,400, 600, fill='red', width=20)
dash = canvas.create_line(0,200,600,200, fill='red', width=20)
iverson = canvas.create_line(0,400,600, 400, fill='red', width=20)

def move(event):
    x=event.x
    y=event.y
    
      
    canvas.create_oval(x-50,y-50,x+50,y+50, fill='white', width=20) 
canvas.bind('<ButtonPress-1>', move)
def move2(event):
    x=event.x
    y=event.y
    canvas.create_line( x-50,y-50,x+50,y+50, width=20)
    canvas.create_line( x-50,y+50,x+50,y-50, width=20)
canvas.bind('<ButtonPress-1>', move)
canvas.bind('<ButtonPress-3>', move2)
root.mainloop()