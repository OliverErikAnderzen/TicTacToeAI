import pygame

class View:
    def __init__(self, model):
        self.model = model
        self.grid_size = model.grid_size
        self.cell_size = model.cell_size
        self.screen = pygame.display.set_mode(
            (self.grid_size[0] * self.cell_size, self.grid_size[1] * self.cell_size)
        )
        pygame.display.set_caption("TicTacToeAI")

    def draw_segment(self, x, y, color):
        cs = self.cell_size
        pygame.draw.rect(self.screen, color, (cs*x, cs*y, cs, cs))

    def render(self):
        grid_size = self.model.grid_size
        cell_size = self.model.cell_size