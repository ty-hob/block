import pygame


pygame.font.init()
font = pygame.font.SysFont("comicsansms", 20)

def player(x, y, surface):
    pygame.draw.rect(surface, (102, 255, 102), [x, y, 40, 80])

#ui

def inventory(x, y, surface):
    pygame.draw.rect(surface, (153, 153, 102), [x, y, 206, 165]) 
    for i in range(6):
        pygame.draw.line(surface, (0, 0, 0), [x+(i*41), y], [x+(i*41), y+164], 2)
    for i in range(5):
        pygame.draw.line(surface, (0, 0, 0), [x, y+(i*41)], [x+205, y+(i*41)], 2)

def inventory_currsor_empty(x, y, surface):
    pygame.draw.rect(surface, (204, 255, 51), [x, y, 42, 42], 4)

def inventory_currsor_full(x, y, surface):
    pygame.draw.rect(surface, (255, 153, 102), [x, y, 42, 42], 4)

def hotbar(x, y, surface):
    pygame.draw.rect(surface, (153, 153, 102), [x, y, 206, 42]) 
    for i in range(6):
        pygame.draw.line(surface, (0, 0, 0), [x+(i*41), y], [x+(i*41), y+41], 2)
    for i in range(2):
        pygame.draw.line(surface, (0, 0, 0), [x, y+(i*41)], [x+205, y+(i*41)], 2)

def hotbar_currsor(x, y, surface):
    pygame.draw.rect(surface, (204, 153, 0), [x, y, 42, 42], 4)

def block_breaking_progress_bar(x, y, surface, progress):
    pygame.draw.rect(surface, (153, 153, 102), [x, y, 100, 20])
    pygame.draw.rect(surface, (0, 200, 0), [x, y, progress, 20])
    pygame.draw.rect(surface, (0, 0, 0), [x, y, 100, 20], 3)

# blocks

def air(x, y, surface):
    pass

def dirt(x, y, surface):
    pygame.draw.rect(surface, (79, 60, 42), [x, y, 40, 40])
    #77, 40, 0

def grass(x, y, surface):
    dirt(x, y, surface)
    pygame.draw.rect(surface, (51, 102, 0), [x, y, 40, 10])

def stone(x, y, surface):
    pygame.draw.rect(surface, (64, 64, 64), [x, y, 40, 40])

def sand(x, y, surface):
    pygame.draw.rect(surface, (200, 200, 0), [x, y, 40, 40])

def water(x, y, surface):
    pygame.draw.rect(surface, (51, 102, 255), [x, y, 40, 40])

def tree_leafes(x, y, surface):
    pygame.draw.rect(surface, (23, 53, 18), [x, y, 40, 40])

def tree_stump(x, y, surface):
    pygame.draw.rect(surface, (86, 47, 14), [x+10, y, 20, 40])

# items

def dirt_item(x, y, surface, amount):
    t = font.render(str(amount), True, (0, 0, 0))
    pygame.draw.rect(surface, (79, 60, 42), [x, y, 30, 30])
    surface.blit(t, [x+20, y+20])

def stone_item(x, y, surface, amount):
    t = font.render(str(amount), True, (0, 0, 0))
    pygame.draw.rect(surface, (64, 64, 64), [x, y, 30, 30])
    surface.blit(t, [x+20, y+20])

def sand_item(x, y, surface, amount):
    t = font.render(str(amount), True, (0, 0, 0))
    pygame.draw.rect(surface, (200, 200, 0), [x, y, 30, 30])
    surface.blit(t, [x+20, y+20])

def wood_pickaxe_item(x, y, surface, amount):
    #122, 77, 31
    pygame.draw.rect(surface, (122, 77, 31), [x+8, y, 6, 30])
    pygame.draw.rect(surface, (81, 51, 21), [x+3, y, 18, 3])
    pygame.draw.rect(surface, (81, 51, 21), [x+3, y+3, 24, 3])

# tools

def wood_pickaxe_tool(x, y, surface):
    pygame.draw.rect(surface, (122, 77, 31), [x, y, 8, -60])
    pygame.draw.rect(surface, (81, 51, 21), [x-4, y-50, 18, -8])
    pygame.draw.rect(surface, (81, 51, 21), [x+14, y-50, 8, -4])