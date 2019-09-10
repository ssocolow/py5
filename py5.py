#importing tkinter
import tkinter as tk

#initialize global variables
mainwindow = 0
canvas = 0
width = 0
height = 0

#make a canvas function
def createCanvas(w, h):
    #use global variables
    global mainwindow
    global width
    global height
    global canvas
    
    #make the window
    mainwindow = tk.Tk()
    
    width = w
    height = h
    
    #make the canvas with the correct width and height in the window
    canvas = tk.Canvas(mainwindow, width=width, height=height)
    
    #pack canvas (this helps the geometry organizer)
    canvas.pack()
    return canvas

#make a line function
def line(x0, y0, x1, y1, color='blue'):
    #use global variables
    global canvas
    global mainwindow
    
    id = canvas.create_line(x0, y0, x1, y1, fill=color)
    mainwindow.update()
    return id

#make an ellipse function
def ellipse(x0, y0, x1, y1, color='blue'):
    #use global variables
    global canvas
    global mainwindow
    
    id = canvas.create_oval(x0, y0, x1, y1, fill=color)
    mainwindow.update()
    return id

#make a rectangle function
def rect(x0, y0, x1, y1, color='blue'):
    #use global variables
    global canvas
    global mainwindow
    
    id = canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    mainwindow.update()
    return id

#update the screen
def draw():
    mainwindow.update()

#mainloop enters an infinite loop of drawing (useful for static and non responsive graphics) (I think)
def show():
    mainwindow.mainloop()
