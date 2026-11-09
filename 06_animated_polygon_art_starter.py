import turtle
import time
import math
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)

polygons = [
    Polygon(-200, 0, 3, 60, "red", 4),
    Polygon(-150, 50, 4, 70, "cyan", 3),
    Polygon(-100, 0, 5, 60, "yellow", 4),
    Polygon(-50, 50, 6, 55, "green", 3),
    Polygon(0, 0, 7, 50, "orange", 4),
    Polygon(50, 50, 8, 45, "purple", 3),
    Polygon(100, 0, 5, 65, "pink", 4),
    Polygon(150, 50, 3, 70, "white", 3)
]

for polygon in polygons:
    polygon.draw()

screen.update()

for frame in range(70):
    for i, polygon in enumerate(polygons):

        x = -200 + i * 50 + math.sin(frame * 0.08 + i) * 50
        y = math.cos(frame * 0.08 + i) * 70

        polygon.move_to(x, y)

    screen.update()
    time.sleep(0.05)

screen.mainloop()