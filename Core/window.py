import pygame

class Window:

    def __init__(self, dimensions, caption='UnnamedEnvironment', background_color = [255, 255, 255]):
        pygame.init()
        pygame.display.init()

        self.dimensions = dimensions
        self.background_color = background_color
        self.captions = caption
        self.window = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(caption)

    def set_icon(self, icon_image):
        self.window.set_icon(icon_image)

    def add_gameobject(self, gameobject):
        self.window.blit(gameobject.get_sprite(), gameobject.transform.pos)

    def set_background_color(self, color):
        self.background_color = color

    def window_functionality(self):
        self.window.fill(self.background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate_app()

    def terminate_app(self):
        pygame.quit()
        quit()