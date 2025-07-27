from utils import randbbool

class Cloud:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def update_clouds(self, r = 2, mxr = 15, g = 4, mxg = 15):
        for i in range(self.h):
            for j in range(self.w):
                if randbbool(r, mxr):
                    self.cells[i][j] = 1
                    if randbbool (g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]