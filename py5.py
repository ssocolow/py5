import tkinter as tk

mainwindow = 0
canvas = 0
width = 0
height = 0

def createCanvas(w, h):
    global mainwindow
    global width
    global height
    global canvas

    mainwindow = tk.Tk()
    
    width = w
    height = h

    canvas = tk.Canvas(mainwindow, width=width, height=height)

    canvas.pack()
    return canvas


def line(x0, y0, x1, y1, color='blue'):
    global canvas
    global mainwindow
    
    id = canvas.create_line(x0, y0, x1, y1, fill=color)
    mainwindow.update()
    return id

def ellipse(x0, y0, x1, y1, color='blue'):
    global canvas
    global mainwindow
    
    id = canvas.create_oval(x0, y0, x1, y1, fill=color)
    mainwindow.update()
    return id

def rect(x0, y0, x1, y1, color='blue'):
    global canvas
    global mainwindow
    
    id = canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    mainwindow.update()
    return id

def draw():
    mainwindow.update()

def show():
    mainwindow.mainloop()


#createCanvas(500,500)
#line(0,500,500,0)
#rect(25,200,80,300)
#ellipse(200,50,300,450)


#x = 500
#while(x > 0):
 #   line(x,500,500,0, 'blue')
  #  x -= 1
   # time.sleep(0.01)
