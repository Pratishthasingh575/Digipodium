from turtle import *
speed('fastest')
color = ['red','blue']
bgcolor('black')
for i in range(7):
    pencolor('blue')
    pensize('2')
    fd(130)
    for i in range(6):
        pencolor('purple')
        fd(70)
        fillcolor(color[i%2])
        begin_fill()
        for i in range(3):
            pencolor('purple')
            fd(25)
            lt(360/3)
        end_fill()
        lt(360/6)
    lt(360/7)
    
mainloop()
