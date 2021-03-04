import mss
from pynput.keyboard import Controller
from pynput.keyboard import Listener
from time import sleep
from random import randint
import threading
import sys

from pynput.keyboard import Key

class OsuBot:

    def __init__(self, mode='7k', bind_key=Key.num_lock, quit_key=Key.esc, note_delay=0.004,
                 monitor={"top": 860, "left": 300, "width": 500 + 250, "height": 28}, y_center=0,
                 note_height=25, thres=65):

        self.bind_key = bind_key
        self.quit_key = quit_key
        self.note_delay = note_delay
        self.monitor = monitor
        self.y_center = y_center
        self.note_height = note_height
        self.thres = thres
        self.noteAction = self.hit
        self.combo = 0

        if mode == '10k':
            self.keys = {'q': 40, 'w': 110, 'e': 175, 'r': 240, 't': 310, 'y': 466, 'u': 532, 'i': 600, 'o': 668,
                         'p': 735}
        else:
            self.keys = {'q': 40, 'w': 110, 'e': 175, 'r': 240, 't': 310, 'y': 375, 'u': 445}

        self.cont = Controller()
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        self.MainThread = StoppableThread(target=self.key_loop, daemon=True)

        for key in self.keys.keys():
            self.cont.release(key)

    def key_loop(self):
        prev = {'q': False, 'w': False, 'e': False, 'r': False, 't': False, 'y': False, 'u': False, 'i': False,
                'o': False,
                'p': False}
        with mss.mss() as sct:
            while True:
                img = sct.grab(self.monitor)
                ks = self.getKeys(img)

                if len(ks) != 0:
                    for c, future in ks:
                        if prev[c] == False:
                            self.noteAction(self, c)
                    sleep(self.note_delay)
                    for c, future in ks:
                        if future:
                            prev[c] = True
                        if not future:
                            self.cont.release(c)
                            prev[c] = False

    @staticmethod
    def hit(bot, key):
        bot.cont.press(key)

    @staticmethod
    def getHit():
        R = randint(1, 100)
        if R == 1:
            return 0
        elif R <= 5:
            return 0.01
        else:
            return 0

    def getKeys(self, sct):
        valid = []
        for key in self.keys.items():

            intens1 = 0
            for i in range(3):
                p1 = sct.pixel(key[1], 2 + self.note_height + self.y_center - i)
                temp = ((p1[0] + p1[1] + p1[2]) / 3)
                if temp > intens1:
                    intens1 = temp

            # p1 = sct.pixel(key[1], note_height+y_center)
            # intens1 = ((p1[0] + p1[1] + p1[2]) / 3)

            p2 = sct.pixel(key[1], 0)
            intens2 = ((p2[0] + p2[1] + p2[2]) / 3)

            # p3 = sct.pixel(keys_black[key[0]], 0)
            # intens_long = ((p3[0] + p3[1] + p3[2]) / 3)

            # intens1 = 0
            # intens2 = 0
            # for i in range(2):w
            #     for j in range(2):
            #         p1 = sct.pixel(key[1] + i, y_center+note_height + j)
            #         intens1 = intens1 + ((p1[0] + p1[1] + p1[2])/3)/9
            #
            #         p2 = sct.pixel(key[1] + i, y_center + j)
            #         intens2 = intens2 + ((p2[0] + p2[1] + p2[2])/3)/9

            if intens1 > self.thres:
                # print(key[0] + ' ' + str(intens1))
                if intens2 > self.thres:
                    valid.append((key[0], True))
                else:
                    valid.append((key[0], False))
        return valid

    def on_press(self, key):
        if (key == self.quit_key):
            try:
                print("Thread killed")
                self.MainThread.stop()
                self.MainThread = StoppableThread(target=self.key_loop, daemon=True)
            except(ValueError):
                print("Bot not running")
                pass

        if (key == self.bind_key):
            # Begin game
            self.MainThread.start()
            print("Begin...")

#This sucks right now
class StoppableThread(threading.Thread):

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        sys.exit()

    def stopped(self):
        return self._stop_event.is_set()