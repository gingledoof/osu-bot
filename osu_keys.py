
import mss
from pynput.keyboard import Controller
from pynput.keyboard import Listener
from time import sleep
from random import randint
from utils import *
import multiprocessing

cont = Controller()

for key in keys.keys():
    cont.press(key)
    cont.release(key)

def getKeys(sct):
    valid = []
    for key in keys.items():

        intens1 = 0
        for i in range(3):
            p1 = sct.pixel(key[1], 2 +note_height + y_center - i)
            temp = ((p1[0] + p1[1] + p1[2]) / 3)
            if temp > intens1:
                intens1 = temp


        #p1 = sct.pixel(key[1], note_height+y_center)
        #intens1 = ((p1[0] + p1[1] + p1[2]) / 3)

        p2 = sct.pixel(key[1], 0)
        intens2 = ((p2[0] + p2[1] + p2[2]) / 3)

        #p3 = sct.pixel(keys_black[key[0]], 0)
        #intens_long = ((p3[0] + p3[1] + p3[2]) / 3)

        # intens1 = 0
        # intens2 = 0
        # for i in range(2):w
        #     for j in range(2):
        #         p1 = sct.pixel(key[1] + i, y_center+note_height + j)
        #         intens1 = intens1 + ((p1[0] + p1[1] + p1[2])/3)/9
        #
        #         p2 = sct.pixel(key[1] + i, y_center + j)
        #         intens2 = intens2 + ((p2[0] + p2[1] + p2[2])/3)/9


        if intens1 > thres:
            #print(key[0] + ' ' + str(intens1))
            if intens2 > thres:
                valid.append((key[0], True))
            else:
                valid.append((key[0], False))
    return valid

def key_loop():
    prev = {'q': False, 'w': False, 'e': False, 'r': False, 't': False, 'y': False, 'u': False, 'i': False, 'o': False,
            'p': False}
    with mss.mss() as sct:
        while True:
            img = sct.grab(monitor)
            ks = getKeys(img)

            if len(ks) != 0:
                for c, future in ks:
                    if prev[c] == False:
                        #sleep(getHit())
                        cont.press(c)
                sleep(note_delay)
                for c, future in ks:
                    if future:
                        prev[c] = True
                    if not future:
                        cont.release(c)
                        prev[c] = False

T = multiprocessing.Process(target =key_loop)
def on_press(key):
    if (key == quit_key):
        if T.is_alive():
            print("Thread killed")
            T.kill()
        else:
            print("Not running")

    if (key == bind_key):
        #Begin game
        if not T.is_alive():
            print("Begin...")
            T.start()


def getHit():
    R=randint(1,100)
    if R == 1:
        return 0
    elif R <= 5:
        return 0.01
    else:
        return 0

listener = Listener(
    on_press=on_press)
listener.start()
