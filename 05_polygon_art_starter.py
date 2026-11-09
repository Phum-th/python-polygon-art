import turtle
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Polygon Art")
screen.bgcolor("black")
screen.tracer(0)

polygons = [
    Polygon(-250, 100, 3, 100, "red", 4, 10),
    Polygon(-150, 150, 4, 90, "cyan", 3, 20),
    Polygon(-50, 100, 5, 80, "yellow", 5, 30),
    Polygon(50, 150, 6, 70, "green", 3, 15),
    Polygon(150, 100, 7, 65, "orange", 4, 25),

    Polygon(-250, -50, 4, 120, "blue", 5, 10),
    Polygon(-150, -100, 5, 90, "purple", 3, 40),
    Polygon(-50, -50, 3, 110, "pink", 4, 20),
    Polygon(50, -100, 6, 80, "white", 3, 30),
    Polygon(150, -50, 5, 100, "magenta", 5, 15),

    Polygon(-200, 0, 7, 60, "gold", 3, 45),
    Polygon(-100, 50, 3, 75, "lime", 4, 60),
    Polygon(0, 0, 8, 55, "cyan", 3, 20),
    Polygon(100, 50, 4, 85, "red", 5, 35),
    Polygon(200, 0, 6, 70, "orange", 3, 50)
]

for polygon in polygons:
    polygon.draw()

screen.update()
screen.mainloop()