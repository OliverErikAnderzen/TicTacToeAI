import pygame

class View:
    def __init__(self, model):
        self.model = model

    def render(self):
        grid_size = self.model.grid_size
        cell_size = self.model.cell_size