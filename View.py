import pygame

class View:
    def __init__(self, model):
        self.model = model
        self.grid_size = model.grid_size
        self.cell_size = model.cell_size
        self.x_img = pygame.image.load('pieces/x_piece.png')
        self.o_img = pygame.image.load('pieces/o_piece.png')
        self.x_img = pygame.transform.scale(self.x_img, (self.cell_size - 20, self.cell_size - 20))
        self.o_img = pygame.transform.scale(self.o_img, (self.cell_size - 20, self.cell_size - 20))
        self.screen = pygame.display.set_mode(
            (self.grid_size[0] * self.cell_size, self.grid_size[1] * self.cell_size)
        )
        pygame.display.set_caption("TicTacToeAI")

    def draw_segment(self, x, y, color):
        cs = self.cell_size
        pygame.draw.rect(self.screen, color, (cs*x, cs*y, cs, cs))

    def draw_board(self):
        self.draw_segment(0,0,(207,185,151))
        self.draw_segment(0,2,(207,185,151))
        self.draw_segment(1,1,(207,185,151))
        self.draw_segment(2,0,(207,185,151))
        self.draw_segment(2,2,(207,185,151))

    def draw_pieces(self):
        rep = self.model.game_representation
        
        for row in range(3):
            for col in range(3):
                if rep[row][col] == "X":
                    self.screen.blit(self.x_img, (col * self.cell_size + 10, row * self.cell_size + 10))
                if rep[row][col] == "O":
                    self.screen.blit(self.o_img, (col * self.cell_size + 10, row * self.cell_size + 10))

    def render(self):
        self.screen.fill((250, 235, 240))
        self.draw_board()
        self.draw_pieces()
        pygame.display.flip()