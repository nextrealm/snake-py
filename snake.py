import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Snake')

snake = []
direction = 1
for n in range(0, 4):
    self.pieces.append((self.startX, self.startY + n))
pos = [1, 1]
snake.append(pos)
food = [random.randint(1, self.sizeX)]

clock = pygame.time.Clock()

def move(piece):
    if direction == 1: piece[0] += 1
    elif direction == 2: piece[1] += 1
    elif direction == 3: piece[0] -= 1
    elif direction == 4: piece[1] -= 1

def check(piece):
    if piece[0] == food[0] and piece[1] == food[1]: return true
    return false

def point(new_direction):
    if direction == 1 and new_direction == 3: return
    if direction == 3 and new_direction == 1: return
    if direction == 2 and new_direction == 4: return
    if direction == 4 and new_direction == 2: return
    direction = new_direction

while true:
    pygame.event.pump()
    keys = pygame.key.get_pressed() 
    if (keys[K_RIGHT]):
        point(1)
    elif (keys[K_DOWN]):
        point(2)
    elif (keys[K_LEFT]):
        point(3)
    elif (keys[K_UP]):
        point(4)
    
    tail = snake[-1]
    # tail = snake.pop()
    move(tail)
    remove = check(snake[0])
    if remove: snake.pop()
    snake.insert(0, tail)

    screen.fill(BLACK)
    for (px, py) in snake: 
        pygame.draw.rect(screen, WHITE, (10 * px, 10 * py, 10, 10))
    pygame.draw.rect(screen, RED, (10 * food[0], 10 * food[1], 10, 10))
    pygame.display.flip()
pygame.quit()
