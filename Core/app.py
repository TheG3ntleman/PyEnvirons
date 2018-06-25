import pygame

class App:

    def __init__(self, window, FPS=60):
        self.window = window
        self.running = False
        self.FPS = FPS
        self.Clock = pygame.time.Clock()
        self.layers = []

    def run(self):
        self.running = True
        self.game_loop()

    def add_layer(self, layer):
        self.layers.append(layer)

    def game_loop(self):
        while self.running:
            self.window.window_functionality()

            for layer in self.layers:
                for gameobject in layer.components:
                    gameobject.object_update()
                    self.window.add_gameobject(gameobject)

            pygame.display.update()
            self.Clock.tick(self.FPS)