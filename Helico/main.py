# 🚁☁️🔥🟩🌲💛🌊🪣⚡🏦🏥🏆

from map import Map
from pynput import keyboard
import time
import os
from helicopter import Helicopter as Helico
from clouds import Cloud
import json


TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 200
CLOUD_UPDATE = 200
MAP_W, MAP_H = 30, 15

tmp = Map(MAP_W, MAP_H)
clouds = Cloud(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)
tick = 1

MOVES = {'w': (-1, 0), 'a': (0, -1), 's': (1, 0), 'd': (0, 1)}

def on_release(key):
    global helico, tick, clouds, tmp
    try:
        if hasattr(key, 'char') and key.char: c = key.char.lower()
        else: ''
        # print(c)
    #except: print("Бабайка")
        if c in MOVES.keys():
            dx, dy = MOVES[c][0], MOVES[c][1]
            helico.move(dx, dy)
        elif c == 'f':
            data = {"helicopter": helico.export_data(),
                        "clouds": clouds.export_data(),
                        "field": tmp.export_data(),
                        "tick": tick}
            with open("level.json", "w") as lvl:
                json.dump(data, lvl)
        elif c == 'g':
            with open("level.json", "r") as lvl:
                data = json.load(lvl)
                print(data["tick"])
                helico.import_data(data["helicopter"])
                tick = data["tick"] or 1
                tmp.import_data(data["field"])
                clouds.import_data(data["clouds"])
        # print("DEBUG data:", data)
        # print("DEBUG helicopter data:", data["helicopter"])

    except Exception as e:
        print("Бабайка")
    
listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()


while True:
    os.system("cls")
    print("TICK", tick)
    tmp.process_helicopter(helico,clouds)
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