import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game with ball")

radius = 50
run = True

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    cursor = pygame.mouse.get_pos()
    x = cursor[0]
    if cursor[0] > 750:
        x = 750
    elif cursor[0] < 50:
        x = radius
    print(cursor)
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (80, 243, 102), (x, 400), radius)
    pygame.display.update()


