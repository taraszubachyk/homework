import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game with ball")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    cursor = pygame.mouse.get_pos()
    # print(cursor)
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (80, 243, 102), (cursor[0], 400 ), 50) #cursor[1]
    pygame.display.update()


