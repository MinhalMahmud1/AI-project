import pygame
from halma.constants import *
from halma.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halma")


def get_row_col_from_mouse(pos):
    """
    Get the row and column of the square that the mouse is currently hovering over.

    Parameters:
        pos (tuple): The position of the mouse on the window.

    Returns:
        A tuple containing the row and column of the square.
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    """
    The main game loop. Initializes the game and updates the game state
    based on user input and AI moves.
    """
    run = True
    game_over = False  # Flag to check if the game has ended
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        # AI makes a move
        if game.turn == WHITE and not game_over:  # AI only plays if the game is not over
            value, new_board = minimax(game.get_board(), 2, float('-inf'), float('inf'), WHITE, game)
            game.ai_move(new_board)

        # Check for a winner
        winner = game.winner()
        if winner is not None and not game_over:
            print(f"{winner} ")  # Print the winner once
            game_over = True  # Set the flag to stop further actions

        # Check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Checks for user mouse click input
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        # Update the game window
        game.update()

    pygame.quit()



main()
