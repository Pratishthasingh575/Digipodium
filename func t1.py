from turtle import*

def square(size,color='blue'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
      fd(size)
      rt(90)
    end_fill()

 
def hexagon(size,color='blue'):
    fillcolor(color)
    begin_fill()
    for i in range(6):
      fd(size)
      rt(60)

square(150,'red') 
square(100,'blue') 
square(50,'green') 
square(25,'purple') 
hexagon(116)
hexagon(50)
hexagon(25,'pink')
square(25,'yellow')

mainloop()
