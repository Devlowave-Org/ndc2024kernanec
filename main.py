import pyxel


class LightCircle:
    """
    Ce cercle Lumineux a exactement les meme coordonnées que le personnage
    Il est placé 1 Layer au dessus dans le draw.
    """
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.mid_x = pyxel.width // 2 - self.width // 2
        self.mid_y = pyxel.height // 2 - self.height // 2

    def update(self):
        pass

    def draw(self, x, y):
        pyxel.blt(x + self.mid_x, y + self.mid_y, 0, 0, 0, 64, 64, 11)


class Golum:
    def __init__(self, x, y, w, h):
        self.deplacement = {pyxel.KEY_Z: (0, -2, "up"), pyxel.KEY_S: (0, 2, "down"), pyxel.KEY_Q: (-2, 0, "left"),
                            pyxel.KEY_D: (2, 0, "right")}
        self.direction = "up"
        self.costumes = {"up": (0, 64, 32, 32), "down": (32, 64, 32, 32), "left": (64, 64, 32, 32), "right": (96, 64, 32, 32)}
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.mid_x = pyxel.width // 2 - self.width // 2
        self.mid_y = pyxel.height // 2 - self.height // 2

    def collisions(self):
        dir_offset = {"up": (self.mid_x, self.mid_y - 1), "down": (self.x, self.y + self.height), "left": (self.x - 1, self.y), "right": (self.x + self.width, self.y)}
        if self.direction == "up" or self.direction == "down":
            for i in range(self.width):
                if pyxel.pget(self.mid_x, self.mid_y) == 3:
                    pyxel.rect(dir_offset[self.direction][0] + self.mid_x + i, dir_offset[self.direction][1] + self.mid_y, 1, 1, 6)
                else:
                    pass
        else:
            for i in range(self.height):
                if pyxel.pget(self.mid_x, self.mid_y) == 3:
                    pyxel.rect(dir_offset[self.direction][0] + self.mid_x, dir_offset[self.direction][1] + self.mid_y + i, 1, 1, 6)
                else:
                    pass
    def movement(self):
        for key, value in self.deplacement.items():
            if pyxel.btn(key):
                self.x += self.deplacement[key][0]
                self.y += self.deplacement[key][1]
                self.direction = self.deplacement[key][2]

    def update(self):
        self.movement()
        pyxel.camera(self.x, self.y)

    def draw(self):
        """
        version dessinée
        if pyxel.frame_count % 2 == 0:
            pyxel.blt(self.x + self.mid_x, self.y + self.mid_y, self.costume[self.direction][0], self.costume[self.direction][1] + 32, self.costume[self.direction][2], self.costume[self.direction][3])
        else:
            pyxel.blt(self.x + self.mid_x, self.y + self.mid_y, self.costume[self.direction][0], self.costume[self.direction][1] + 32, self.costume[self.direction][2], self.costume[self.direction][3])
        """
        pyxel.rect(self.x + self.mid_x, self.y + self.mid_y, self.width, self.height, 3)
        self.collisions()


class App:
    def __init__(self):
        pyxel.init(256, 256, fps=60)
        pyxel.load("theme2dev.pyxres")
        self.golum = Golum(0, 0, 32, 32)
        self.lightcircle = LightCircle(64, 64)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.golum.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, pyxel.width, pyxel.height, 11)
        self.golum.draw()
        self.lightcircle.draw(self.golum.x, self.golum.y)


App()
