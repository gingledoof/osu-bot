
import mss
from pynput import keyboard
from pynput.keyboard import Controller
from time import sleep

cont = Controller()
note_height = 25
monitor = {"top": 895-note_height, "left": 300, "width": 500+250, "height": 3+note_height}
thres = 70

y_center = 0
keys = {'q': 40, 'w': 110, 'e': 175, 'r': 240, 't': 310, 'y': 375, 'u': 445}

keys10k = {'q': 40, 'w': 110, 'e': 175, 'r': 240, 't': 310, 'y': 466, 'u': 532, 'i': 600, 'o': 668, 'p': 735}
keys_black10k = {'q': 10, 'w': 80, 'e': 145, 'r': 215, 't': 280, 'y': 440, 'u': 507, 'i': 575, 'o': 641, 'p': 709}

keys_black = {'q': 10, 'w': 80, 'e': 145, 'r': 215, 't': 280, 'y': 350, 'u': 415}

def getKeys(sct):
    valid = []
    for key in keys10k.items():

        intens1 = 0
        for i in range(4):
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
        # for i in range(2):
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


import random
def on_press(key):

    def getHit():
        R=random.randint(1,100)
        if R == 1:
            #200 Hit
            return 0
        elif R <= 20:
            return  0.0005
        else:
            return 0

    if (key == keyboard.Key.num_lock):
        #Begin game
        print("Begin...")
        prev = {'q': False, 'w': False, 'e': False, 'r': False, 't': False, 'y': False, 'u': False, 'i': False, 'o': False, 'p': False}
        with mss.mss() as sct:
            while True:
                img = sct.grab(monitor)
                ks = getKeys(img)
                #mss.tools.to_png(img.rgb, img.size, output="out.png")

                if len(ks) != 0:
                    for c, future in ks:
                        if prev[c] == False:
                            #sleep(getHit())
                            cont.press(c)
                    sleep(0.003)
                    for c, future in ks:
                        if future:
                            prev[c] = True
                        if not future:
                            cont.release(c)
                            prev[c] = False


listener = keyboard.Listener(
    on_press=on_press)
listener.start()
