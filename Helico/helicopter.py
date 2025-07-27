from utils import randcell
import os


class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.mxtank = 2
        self.tank = 0
        self.score = 0
        self.life = 500
        
    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_menu (self):
        print("🏆   ", self.score, end=" | ")
        print("💛   ", self.life, end=" | ")
        print("🪣   ", self.tank, "/", self.mxtank, sep="")

    def game_over(self):
        global helico
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XX  GAME OVER, YOUR SCORE IS", self.score,"XX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)

    def export_data(self):
        return {"score": self.score,
                "life": self.life,
                "x": self.x, "y": self.y,
                "tank": self.tank, "mxtank": self.mxtank}
    
    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 1
        self.mxtank = data["mxtank"] or 2
        self.life = data["life"] or 500
        self.score = data["score"] or 0