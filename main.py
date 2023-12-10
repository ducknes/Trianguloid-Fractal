import turtle
import random


def draw_trianguloid(turtle, iterations):
    x, y = 0.5, 0.75

    for _ in range(iterations):
        a = random.random()

        if a <= 1/3:
            x1 = 2 * x * y / (x**2 + y**2)
            y1 = (y**2 - x**2) / (y**2 + x**2)
        elif a <= 2/3:
            x1 = 2 / (x + 2) - 1
            y1 = 2 / (y + 2) - 1
        else:
            x1 = (x**2 - y**2) / (x**2 + y**2)
            y1 = 2 * x * y / (y**2 + x**2)

        x, y = x1, y1
        turtle.penup()
        turtle.goto(x * 200, y * 200)
        turtle.pendown()
        turtle.dot(5, "black")


def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Trianguloid Fractal")

    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(99999999999999)

    draw_trianguloid(fractal_turtle, 5000)

    window.exitonclick()


if __name__ == "__main__":
    main()
