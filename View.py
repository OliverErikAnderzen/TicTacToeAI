import pygame

class View:
    def __init__(self, model):
        self.model = model
        self.grid_size = model.grid_size
        self.cell_size = model.cell_size