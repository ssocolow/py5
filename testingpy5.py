from py5 import *
import time

c = createCanvas(500,500)

ball = ellipse(1,0,50,50)

vel = 1
speed = 5
nspeed = -1 * speed

while(True):
    if c.coords(ball)[0] < 450 and vel == 1:
        c.move(ball, speed, 0)
    if c.coords(ball)[0] >= 450:
        vel = -1
        c.move(ball, nspeed, 0)
    if c.coords(ball)[0] < 450 and vel == -1:
        c.move(ball, nspeed, 0)
    if c.coords(ball)[0] <= 0:
        vel = 1
        c.move(ball, speed, 0)
    time.sleep(0.01)
    draw()
