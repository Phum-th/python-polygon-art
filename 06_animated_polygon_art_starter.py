
import turtle
import random
import math
import time
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)

rng = random.Random(17)
colors = ["cyan", "springgreen", "orange",
          "deepskyblue", "plum", "yellow"]

shapes = []

for _ in range(12):
    x = rng.randint(-290, 210)
    y = rng.randint(-170, 120)

    shape = Polygon(
        x, y,
        rng.randint(3, 6),
        rng.randint(35, 105),
        rng.choice(colors),
        rng.randint(1, 6),
        rng.randint(0, 359)
    )

    shape.draw()

    shapes.append((shape, x, y, rng.random() * 6.28))

for frame in range(100):
    for shape, home_x, home_y, phase in shapes:

        x = home_x + 32 * math.cos(frame * 0.07 + phase)
        y = home_y + 23 * math.sin(frame * 0.07 + phase)

        shape.move_to(x, y)

    screen.update()
    time.sleep(0.045)

screen.mainloop()
