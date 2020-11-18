import pygame
pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Colter's Python Memory Game")

icon = pygame.image.load("blankSquare.png")
pygame.display.set_icon(icon)

# player_img = pygame.image.load("brain_coral_fan.png")

class Character:
    def __init__(self, x, y, width, height, speed = 5, color=(0,0,255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
    def draw(self):
        screen.blit(player_img, (self.x, self.y))
    def isClicked(self):
        return mouseState and not oldMouseState and self.rect.collidepoint(mousePos)
    def hoveredOver(self):
        return self.rect.collidepoint(mousePos)
        # pygame.draw.rect(screen, (255, 0, 0), )
# def startOfFrameCode():


tile = Character(200, 50, 40, 60)

# pygame.sprite.collide_rect()
run = True
while run:
    pygame.time.delay(10)
    mouseState = pygame.mouse.get_pressed()[0]
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_F5]:
        run = False

    if mouseState and not oldMouseState:
        print("clicked")

    if tile.isClicked():
        print("tile was clicked")


    screen.fill((0, 200, 0))

    oldMouseState = mouseState
    tile.draw()
    pygame.display.update()
pygame.quit()