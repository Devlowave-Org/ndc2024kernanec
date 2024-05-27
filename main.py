import pyxel

class Golum:
    def __init__(self, x, y, w, h):
        self.deplacement = {pyxel.KEY_Z: (0, -2, "up"), pyxel.KEY_S: (0, 2, "down"), pyxel.KEY_Q: (-2, 0, "left"), pyxel.KEY_D: (2, 0, "right")}
        self.direction = "up"
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def update(self):
        for key, value in self.deplacement.items():
            if pyxel.btn(key):
                self.x += self.deplacement[key][0]
                self.y += self.deplacement[key][1]
        pyxel.camera(self.x, self.y)


    def draw(self):
        pyxel.blt(self.x + 100, self.y + 100, 0, 0, 0, 32, 32)


class App:
    def __init__(self):
        pyxel.init(256, 256, fps=60)
        pyxel.load("theme2dev.pyxres")
        self.golum = Golum(0, 0, 32, 32)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.golum.update()

    def draw(self):
        self.golum.draw()



App()