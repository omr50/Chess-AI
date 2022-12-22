import pygame as p
import ChessEngine


WIDTH, HEIGHT = 512, 512

DIMENSION = 8

SQ_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15
# its better to load image once then on every move
# so performance is a lot better. The loadImages()
# function below is used to do this.
IMAGES = {}


def loadImages():
    pieces = ['bp', 'wp', 'bK', 'wK', 'bR',
              'wR', 'bQ', 'wQ', 'bN', 'wN', 'bB', 'wB']

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))
    print(IMAGES)

# driver
# handle IO and update graphics


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.gameState()
    print(gs.board)
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

# UI for gamestate


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) & 1]
            p.draw.rect(screen, color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if (board[r][c] != '--'):
                print(r, c, board[r][c])
                screen.blit(IMAGES[board[r][c]], (c * SQ_SIZE, r * SQ_SIZE))


if __name__ == '__main__':
    main()
