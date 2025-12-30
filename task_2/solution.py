import turtle


def draw_branch_tree(t: turtle.Turtle, length: float, depth: int, angle: float, ratio: float) -> None:
    """
    Draw a binary fractal tree
    """
    if length <= 0:
        return

    # draw trunk from the current node upwards
    t.forward(length)

    if depth == 0:
        twig = length * ratio
        t.left(angle)
        t.forward(twig)
        t.backward(twig)
        t.right(2 * angle)
        t.forward(twig)
        t.backward(twig)
        t.left(angle)
        # go back to the parent node
        t.backward(length)
        return

    # left branch
    t.left(angle)
    draw_branch_tree(t, length * ratio, depth - 1, angle, ratio)

    # right branch
    t.right(2 * angle)
    draw_branch_tree(t, length * ratio, depth - 1, angle, ratio)

    # restore heading and return to the parent node
    t.left(angle)
    t.backward(length)


def render_tree(depth: int) -> None:
    """
    Render a line-based fractal tree.

    Parameters:
    - depth: recursion depth (non-negative integer)
    """
    depth = max(0, int(depth))
    length = 220.0
    angle = 35.0
    ratio = 0.7

    screen = turtle.Screen()
    screen.title("Fractal Tree (lines)")
    screen.bgcolor("white")

    turtle.tracer(False)
    t = turtle.Turtle(visible=False)
    t.speed(0)
    t.pensize(2)
    t.pencolor("#8b1a1a")  # dark red

    # start from the bottom center, heading up
    height = screen.window_height()
    t.penup()
    t.goto(0, -height / 2 + 40)
    t.setheading(90)
    t.pendown()

    draw_branch_tree(t, length, depth, angle, ratio)

    turtle.update()
    screen.mainloop()


if __name__ == "__main__":
    render_tree(depth=10)
