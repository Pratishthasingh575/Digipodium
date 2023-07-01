from turtle import *
speed('fastest')
for i in range(5):
    pencolor('black')
    pensize('2')
    fd(130)
    for i in range(6):
        pencolor('red')
        fd(70)
        for i in range(3):
            pencolor('purple')
            fd(25)
            lt(360/3)
        lt(360/6)
    lt(360/5)
mainloop()
