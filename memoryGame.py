import pygame
import random
from functools import reduce
pygame.init()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Colter's Python Memory Game")
def loadAsset(imageInAssets):
    tempImage = pygame.image.load("assets\\" + imageInAssets + ".png")
    tempImage.convert()
    return tempImage

icon = loadAsset("clock2")
tileImage = loadAsset("justSquareOutline")
pygame.display.set_icon(icon)

# player_img = pygame.transform.scale(icon, (100, 100))

class Character:
    def __init__(self, x, y, width, height, image,\
                 speed = 5, color=(255,255,255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.isSelected = False
        self.isAnswerTile = False
        self.rect = pygame.draw.rect(screen, self.color,\
                (self.x, self.y, self.width, self.height))
        self.image = pygame.transform.scale(image,
                        (self.width, self.height))
    def draw(self):
        self.rect = pygame.draw.rect(screen, self.color,\
            (self.x, self.y, self.width, self.height))
        screen.blit(self.image, (self.x, self.y))
    def isClicked(self):
        return mouseState and not oldMouseState and \
               self.rect.collidepoint(mousePos)
    def hoveredOver(self):
        return self.rect.collidepoint(mousePos)
    def becomeAnswer(self):
        self.isAnswerTile = True
        self.color = (255,0,0)
    def highlight(self):
        if self.isClicked():
            self.isSelected = not self.isSelected
            if self.isSelected:
                self.color = (0,0,255)
            else:
                self.color = (255,255,255)

        # pygame.draw.rect(screen, (255, 0, 0), )
# def startOfFrameCode():

def makeTiles(curDimension):
    """construct the board"""
    board = []
    tileWidth = (screenWidth//curDimension)
    tileHeight = (screenHeight//curDimension)
    for y in range(curDimension):
        board.append([])
        for x in range(curDimension):
            board[-1].append(Character(
                x*tileWidth,
                y*tileHeight,
            tileWidth, tileHeight, tileImage))
    return board

def makePattern(board):
    '''make answer pattern'''
    allTiles = [[(i, j) for i in range(curDimension)] \
                for j in range(curDimension)]
    # random.shuffle(allTiles)
    allTiles = reduce(lambda x, y: y + x, allTiles)
    for i in range(curDimension):
        # chosen = allTiles.pop()
        chosen = random.choice(allTiles)
        # print("chosen", chosen)
        allTiles.remove(chosen)
        board[chosen[0]][chosen[1]].becomeAnswer()

    # print(allTiles)

    return board

def checkAnswer(curDimension, board):
    isComplete = True
    for y in range(curDimension):
        for x in range(curDimension):
            if board[y][x].isSelected != board[y][x].isAnswerTile:
                isComplete = False
                break
        if isComplete == False:
            break
    if isComplete:
        curDimension += 1
        board = []
        board = makeTiles(curDimension)
        board = makePattern(board)

        return curDimension, board
    return (curDimension,)



# tile = Character(200, 50, 40, 60, tile)
hasDoneOneTimeCode = False
curDimension =3
board = []
# pygame.sprite.collide_rect()
run = True
while run:
    pygame.time.delay(10)
    if hasDoneOneTimeCode == False:
        board = makeTiles(curDimension)
        board = makePattern(board)
        hasDoneOneTimeCode = True
    mouseState = pygame.mouse.get_pressed()[0]
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_F5]:
        run = False

    for y in range(curDimension):
        for x in range(curDimension):
            board[y][x].highlight()
    result = checkAnswer(curDimension, board)
    if len(result) == 2:
        # print("result", result)
        curDimension = result[0]
        board = result[1]

    # if mouseState and not oldMouseState:
    #     print("clicked")


    # screen.fill((0, 200, 0))

    oldMouseState = mouseState
    for y in range(curDimension):
        for x in range(curDimension):
            board[y][x].draw()

    # tileImage.draw()
    pygame.display.update()
pygame.quit()