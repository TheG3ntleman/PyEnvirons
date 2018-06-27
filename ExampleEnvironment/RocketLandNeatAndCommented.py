from PyEnviron import PyEnviron

window_height, window_width = [400, 600]
sprites = PyEnviron.ImageContentLoader({'rocket': 'InbuiltImages/Rocket.png',
           'platform': 'InbuiltImages/Platform.png',
           'background': 'InbuiltImages/Background.png'}).content_dict

window = PyEnviron.Window([window_width, window_height], 'RocketLand V0.0.1')
window.set_icon(sprites['rocket'])

Application = PyEnviron.App(window)
Application.set_FPS(30)

score = 0
land = [(window_width/2)-50, window_height]

keyboard = PyEnviron.Controller(['a', 'd'])

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
        self.GM.set_pos([PyEnviron.randomrange(0, window_width), 0])

    def Logic(self):
        global score

        strokes = keyboard.get_strokes()
        vert_motion = strokes[1] - strokes[0]

        self.GM.set_pos([self.GM.transform.pos[0]+vert_motion, self.GM.transform.pos[1]+self.speed])
        if self.GM.transform.pos[1] == window_height:
            if self.GM.transform.pos[0] > land[0] and self.GM.transform.pos[0] < land[0]+100:
                score +=1
            else:
                score -= 1

            self.reset()

rocket = Rocket([PyEnviron.randomrange(0, window_width), 0], sprites['rocket'])
background = PyEnviron.GameObject(sprites['background'])
background.set_scale([0.4, 0.4])
platform = PyEnviron.GameObject(sprites['platform'])
platform.set_pos([land[0], land[1]-platform.sprite.surface.get_height()])

layer = PyEnviron.Layer()
layer.add_gameobjects([background, platform, rocket.GM])

Application.add_layer(layer)
Application.run()
