import pygame

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_player_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

    def run(self):
        while not self.model.game_over:
            self.view.render()
            action = self.get_player_input()
            if action == "QUIT":
                self.model.set_game_over(True)