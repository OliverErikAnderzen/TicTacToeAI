import pygame

class View:
    def __init__(self, model):
        self.model = model
    def draw_segment(self, x, y, color):
        cs = self.cell_size
        pygame.draw.rect(self.screen, color, (cs*x, cs*y, cs, cs))

    def render(self):
        grid_size = self.model.grid_size
        cell_size = self.model.cell_size