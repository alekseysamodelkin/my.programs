# -----------------------------
# Program by Samodelkin
# -----------------------------


import pygame


def point_to_circle(point, circle):
    a = point[0] - circle[0]
    b = point[1] - circle[1]
    r = circle[2]

    return a ** 2 + b ** 2 <= r ** 2


def point_to_rect(point, rect):
    x = point[0]
    y = point[1]

    left = rect[0]
    right = rect[0] + rect[2]
    top = rect[1]
    bottom = rect[1] + rect[3]

    return left <= x <= right and top <= y <= bottom


def circle_to_circle(circle1, circle2):
    a = circle1[0] - circle2[0]
    b = circle1[1] - circle2[1]
    c = circle1[2] + circle2[2]

    return a ** 2 + b ** 2 <= c ** 2


pygame.init()

SIZE = (1200, 800)
TITLE = "Test_color"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

circle = [600, 400, 100]
rectangle = [500, 300, 200, 200]

case = 3

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    circle2 = [mouse_pos[0], mouse_pos[1], 30]

    if case == 1:
        if point_to_circle(mouse_pos, circle):
            color = RED
        else:
            color = BLUE
    elif case == 2:
        if point_to_rect(mouse_pos, rectangle):
            color = RED
        else:
            color = GREEN
    elif case == 3:
        if circle_to_circle(circle, circle2):
            color = RED
        else:
            color = WHITE

    screen.fill(BLACK)

    if case == 1:
        pygame.draw.circle(screen, color, [circle[0], circle[1]], circle[2])
    elif case == 2:
        pygame.draw.rect(screen, color, [rectangle[0], rectangle[1], rectangle[2], rectangle[3]])
    elif case == 3:
        pygame.draw.circle(screen, color, [circle[0], circle[1]], circle[2])
        pygame.draw.circle(screen, BLUE, [circle2[0], circle2[1]], circle2[2])

    pygame.display.flip()

pygame.quit()
