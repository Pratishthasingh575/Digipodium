from turtle import *
speed('fastest')
bgcolor('black')
color=['red','blue','green','yellow','orange','purple']
i =0
while True:
    pencolor(color[i%5])
    fd(10+i)
    lt(140)
    i+=2
mainloop()    