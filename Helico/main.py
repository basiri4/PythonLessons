# 🚁☁️🔥🟩🌲💛🌊🪣⚡🏦🏥🏆

from map import Map
from pynput import keyboard
import time
import os
from helicopter import Helicopter as Helico
from clouds import Cloud


TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUD_UPDATE = 30
MAP_W, MAP_H = 10, 10

tmp = Map(MAP_W, MAP_H)
clouds = Cloud(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'a': (0, -1), 's': (1, 0), 'd': (0, 1)}

def on_release(key):
    global helico
    try:
        c = key.char
        print(c)
        if c in MOVES.keys():
            dx, dy = MOVES[c][0], MOVES[c][1]
            helico.move(dx, dy)
    except: print("Бабайка")

    
listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()


tick = 1
while True:
    os.system("cls")
    print("TICK", tick)
    tmp.process_helicopter(helico)
    helico.print_menu()
    tmp.print_map(helico, clouds)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fire()
    if (tick % CLOUD_UPDATE == 0):
        clouds.update_clouds()