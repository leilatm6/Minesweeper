import pygame
import minessweeper as m
import time

pygame.init()
numcells =8
nummins = 8
square_size = 50
square_border = 3
offset = 40
heightoffset =  square_size + 2 * square_border 
Width = 500
Height = Width  + 2 * square_border
board = [[False *numcells] for _ in range(numcells)]
WIN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Minesweeper")
font = pygame.font.Font('freesansbold.ttf', 40)
happyface = pygame.image.load("assets/happyface.jpg")
happyface = pygame.transform.scale(happyface, (square_size, square_size))
sadface = pygame.image.load("assets/sadface.jpg")
sadface = pygame.transform.scale(sadface, (square_size, square_size))
redflag = pygame.image.load("assets/redflag.jfif")
redflag = pygame.transform.scale(redflag, (square_size, square_size))
greenflag = pygame.image.load("assets/greenflag.png")
greenflag = pygame.transform.scale(greenflag, (square_size, square_size))
mine = pygame.image.load("assets/mine1.png")
mine = pygame.transform.scale(mine, (square_size, square_size))
#mine = pygame.image.load("assets/minered.jpg")
#mine = pygame.transform.scale(mine, (square_size, square_size))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARKGRAY = (169, 169, 169)
LIGHTGRAY = (211, 211, 211)


"""
    Game Loop
"""
minsweeper = m.Minesweeper(numcells, nummins)
cells = [[None] * numcells for _ in range(numcells)]
run = True
finish = False
loose = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #    elif event.type == timer_event:
    """
        Draw the game board
    """
    square = []
    WIN.fill(WHITE)
    rectreset = pygame.Rect(Width/2 - square_size/2, square_border , square_size, square_size)
    if not finish:
        WIN.blit(happyface, rectreset)
    elif loose == True:
        WIN.blit(sadface, rectreset)
    for i in range(numcells):
        row = []
        for j in range(numcells):
            x = offset + (square_size + square_border) * i
            y = heightoffset + (square_size + square_border) * j
            rect = pygame.Rect(x, y, square_size, square_size)
            if cells[i][j] == None:
                pygame.draw.rect(WIN, DARKGRAY, rect)
            elif cells[i][j] == 'f':
                WIN.blit(greenflag, rect)
            else:
                pygame.draw.rect(WIN, LIGHTGRAY, rect)
                if cells[i][j] != "0":
                    text = font.render(cells[i][j],True,BLACK)
                    textrect = text.get_rect()
                    textrect.center = rect.center
                    WIN.blit(text,textrect)
            if finish:
                if minsweeper.ismine((i,j)) and cells[i][j] != 'f' :
                    WIN.blit(mine, rect)
                if not minsweeper.ismine((i,j)) and cells[i][j] == 'f' :
                    WIN.blit(redflag,rect)

            row.append(rect)
        square.append(row)
    pygame.display.update()
    
    
    lclick, _, rclick = pygame.mouse.get_pressed()
    if lclick or rclick:    
        time.sleep(0.2)
        x, y = pygame.mouse.get_pos()
        if rectreset.collidepoint(x, y):
            cells = [[None] * numcells for _ in range(numcells)]
            minsweeper.__init__(numcells, nummins)
            finish = False
            loose = False
        elif not finish:
            for i in range(numcells):
                for j in range(numcells):
                    if square[i][j].collidepoint(x, y):
                        if rclick:
                            #shoflag
                            if cells[i][j] == 'f':
                                cells[i][j] = None
                            elif  cells[i][j] == None:
                                cells[i][j] = 'f'
                                minsweeper.findmine((i,j))
                                if not minsweeper.remainmine:
                                    finish = True
                                    loose = False
                        elif lclick:
                            if minsweeper.ismine((i,j)):
                                finish = True
                                loose = True
                            else:
                                neighbors = [(i,j)]
                                while neighbors:
                                    i,j = neighbors.pop()
                                    neighborsset= minsweeper.findneighbors((i,j))
                                    cellnumber = 0
                                    for n in neighborsset:
                                        if minsweeper.ismine(n):
                                            cellnumber += 1
                                    cells[i][j] = str(cellnumber)
                                    if cellnumber == 0:
                                        for n in neighborsset:
                                            i,j = n
                                            if cells [i][j] == None:
                                                neighbors.append((i,j))
                        

