import pygame
import time

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_player_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONUP:
                return event

    def run(self):
        while not self.model.get_game_over():
            self.view.render()
            action = self.get_player_input()
            if action == "QUIT":
                self.model.set_game_over(True)
            elif action != None:
                self.model.handle_action(action)

            time.sleep(0.1)