from math import *
from tkinter import *
root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.pack()
central_ball = c.create_oval(110, 110, 510, 510, fill='light green')
ball = c.create_oval(500, 300, 530, 330, fill='red')
degree = 0
x1 = 500
y1 = 300
def motion():
    global degree, x1, y1
    x2 = 300 + (200 * cos(degree * pi / 180))
    y2 = 300 + (200 * sin(degree * pi / 180))
    c.move(ball, x2 - x1, y2 - y1)
    root.after(50, motion)
    degree += 1
    x1 = x2
    y1 = y2
motion()
root.mainloop()