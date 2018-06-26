import PyEnviron
import pygame
import random

window_height, window_width = [400, 600]
window_caption = 'RocketLand V0.0.1'

rocket_image_path = 'InbuiltImages/Rocket.png'
platform_image_path = 'InbuiltImages/Platform.png'
background_image_path = 'InbuiltImages/Background.png'
rocket_sprite = PyEnviron.Sprite(rocket_image_path)
platform_sprite = PyEnviron.Sprite(platform_image_path)
background_sprite = PyEnviron.Sprite(background_image_path)

window = PyEnviron.Window([window_width, window_height], window_caption)
window.set_icon(rocket_sprite)

Application = PyEnviron.App(window)
Application.set_FPS(30)
game_lenght = 10*30

score = 0
land = [(window_width/2)-50, window_height]

class Rocket:

    def __init__(self, position, sprite, speed = 5):
        self.epilen = 0
        self.Sprite = sprite
        self.speed = speed
        self.GM = PyEnviron.GameObject(self.Sprite)
        self.GM.set_rot(180)
        self.GM.set_scale([0.3, 0.3])
        self.GM.set_pos(position)
        self.GM.object_update = self.Logic

    def get_gameobject(self):
        return self.GM

    def reset(self):
        self.GM.set_pos([random.randrange(0, window_width), 0])

    def Logic(self):
        global score
        vert_motion = 0

        for event in Application.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    vert_motion = -self.speed
                elif event.key == pygame.K_d:
                    vert_motion = self.speed

        self.GM.set_pos([self.GM.transform.pos[0]+vert_motion, self.GM.transform.pos[1]+self.speed])
        if self.GM.transform.pos[1] == window_height:
            if self.GM.transform.pos[0] > land[0] and self.GM.transform.pos[0] < land[0]+100:
                score +=1
            else:
                score -= 1

            self.reset()

rocket = Rocket([random.randrange(0, window_width), 0], rocket_sprite)
background = PyEnviron.GameObject(background_sprite)
background.set_scale([0.4, 0.4])
platform = PyEnviron.GameObject(platform_sprite)
platform.set_pos([land[0], land[1]-platform.sprite.surface.get_height()])

layer = PyEnviron.Layer()
background_layer = PyEnviron.Layer()
background_layer.add_gameobject(background)
layer.add_gameobject(platform)
layer.add_gameobject(rocket.GM)

Application.add_layer(background_layer)
Application.add_layer(layer)
Application.run()