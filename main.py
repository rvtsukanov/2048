import sys, pygame
import numpy as np
from env import Game
pygame.init()
field_size = 4
game = Game(field_size)
game.rand(2, 2)
game.field[0, 0] = 2
game.field[0, 1] = 4
game.field[0, 2] = 8
game.field[0, 3] = 16

size = width, height = 400, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("2048")
bg = pygame.Surface((size))
bg.fill(pygame.Color('#bbada0'))
#776e65 - font of numbers
indent = 5
box_size = 90



boxes = []
coords = []

for i in range(field_size ** 2):
    bx = pygame.Surface((box_size, box_size))
    bx.fill(pygame.Color("#eee4da"))
    boxes.append(bx)

while 1:
    screen.blit(bg, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            game.move('up')
            game.next_step()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            game.move('down')
            game.next_step()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            game.move('left')
            game.next_step()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            game.move('right')
            game.next_step()


    for ii in range(4):
        for jj in range(4):
            x = jj * (box_size + 2 * indent) + indent
            y = ii * (box_size + 2 * indent) + indent
            x2 = x + box_size/2 - 18
            y2 = y + box_size/2 - 50
            coords.append((x2, y2))
            screen.blit(boxes[ii + jj], (x, y))


    pygame.font.init()

    myfont = pygame.font.SysFont('clearsans', 70)

    for er in range(game.n ** 2):
        num = str(int(list(np.reshape(game.field, -1))[er]))
        if num == '0':
            continue
        if len(num) == 1:
            myfont = pygame.font.SysFont('clearsans', 70)
            if num == '4':
                textsurface = myfont.render(num, True, (119,110,101))
                screen.blit(textsurface, coords[er])
            if num == '8':
                textsurface = myfont.render(num, True, (242,177,121))
                print(er)
                boxes[er].fill(pygame.Color('#f2b179'))
                #(242,177,121)
                screen.blit(textsurface, coords[er])
        if len(num) > 1:
            myfont = pygame.font.SysFont('clearsans', 55)
            if num == '16':
                textsurface = myfont.render(num, True, (119,110,101))
                #(245,149,99)
                screen.blit(textsurface, (coords[er][0] - 17, coords[er][1] + 8))
            if num == '32':
                textsurface = myfont.render(num, True, (119,110,101))
                #(246, 124, 95)
                screen.blit(textsurface, (coords[er][0] - 17, coords[er][1] + 8))
        else:
            myfont = pygame.font.SysFont('clearsans', 70)
            textsurface = myfont.render(num, True, (119,110,101))
            #(119, 110, 101)
            screen.blit(textsurface, coords[er])

    pygame.display.flip()
    #(249,246,242) - font of colorful boxes