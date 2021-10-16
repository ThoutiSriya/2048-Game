import pygame
from pygame.locals import *
import random
import numpy as np


grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
w = 400
h = 400
spacing = 10
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('2048')
pygame.font.init()
myfont = pygame.font.SysFont('comic sans MS', 30)


def position_grid(grid):
    lst = []
    for i, j in enumerate(grid):
        for k, l in enumerate(j):
            if l == 0:
                lst.append([i, k])
    return lst


def reverse(grid):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(grid[i][3 - j])
    return new_mat


def transp(grid):
    new_mat = [[0 for i in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = grid[j][i]
    return new_mat


def compress(grid):
    new_mat = [[0 for i in range(4)] for i in range(4)]
    for i in range(0, 4):
        pos_new = 0
        for j in range(0, 4):
            if grid[i][j] != 0:
                new_mat[i][pos_new] = grid[i][j]
                pos_new += 1
    return new_mat


def merge(grid):
    for i in range(0, 4):
        for j in range(0, 3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] += grid[i][j + 1]
                grid[i][j + 1] = 0
    return grid


def generate_2(grid, k=2):
    for i in range(0, k):
        pos = random.choice(position_grid(grid))
        grid[pos[0]][pos[1]] = 2
    return grid


def moveLeft(grid):
    st1 = compress(grid)
    st2 = merge(st1)
    st3 = compress(st2)
    st4 = generate_2(st3, k=1)
    return st4


def moveRight(grid):
    st0 = reverse(grid)
    st1 = compress(st0)
    st2 = merge(st1)
    st3 = compress(st2)
    st4 = reverse(st3)
    st5 = generate_2(st4, k=1)
    return st5

def moveUp(grid):
    st0 = transp(grid)
    st1 = compress(st0)
    st2 = merge(st1)
    st3 = compress(st2)
    st4 = transp(st3)
    st5 = generate_2(st4, k=1)
    return st5


def moveDown(grid):
    st0 = transp(grid)
    st = reverse(st0)
    st1 = compress(st)
    st2 = merge(st1)
    st3 = compress(st2)
    st3 = reverse(st3)
    st4 = transp(st3)
    st5 = generate_2(st4, k=1)
    return st5


def draw_rectangle(grid):
    screen.fill((204, 204, 255))
    for i in range(4):
        for j in range(4):
            rect_x = j * w // 4 + spacing
            rect_y = i * h // 4 + spacing
            pygame.draw.rect(screen, (255, 255, 204), (rect_x, rect_y, 80, 80), border_radius=8)
            text_surface = myfont.render(f'{grid[i][j]}', True, (0, 0, 0))
            text_rectangle = text_surface.get_rect(center=(rect_x + 40, rect_y + 40))
            screen.blit(text_surface, text_rectangle)


def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'q'
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return 'u'
                elif event.key == K_DOWN:
                    return 'd'
                elif event.key == K_LEFT:
                    return 'l'
                elif event.key == K_RIGHT:
                    return 'r'
                elif event.key == K_q or event.key == K_ESCAPE:
                    return 'q'


def play(grid):
    grid1 = generate_2(grid, k=2)
    while True:
        draw_rectangle(grid1)
        pygame.display.flip()
        user_int = wait_for_key()
        if user_int == 'quit':
            break
        elif user_int == 'l':
            grid1 = moveLeft(grid1)
        elif user_int == 'r':
            grid1 = moveRight(grid1)
        elif user_int == 'u':
            grid1 = moveUp(grid1)
        elif user_int == 'd':
            grid1 = moveDown(grid1)

play(grid)
