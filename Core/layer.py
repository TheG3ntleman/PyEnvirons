class Layer:

    def __init__(self):
        self.components = []

    def add_gameobject(self, gm):
        self.components.append(gm)