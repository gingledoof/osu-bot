from pynput.keyboard import Key

mode = '10k'
#5k, 6k, 7k, 10k

keys7k = {'q': 40, 'w': 110, 'e': 175, 'r': 240, 't': 310, 'y': 375, 'u': 445}
keys10k = {'q': 40, 'w': 110, 'e': 175, 'r': 240, 't': 310, 'y': 466, 'u': 532, 'i': 600, 'o': 668, 'p': 735}

if mode == '10k':
    keys = keys10k
else:
    keys = keys7k

bind_key = Key.num_lock
quit_key = Key.esc
note_delay = 0.004
note_height = 25
monitor = {"top": 885-note_height, "left": 300, "width": 500+250, "height": 3+note_height}
thres = 65

y_center = 0

#keys_black10k = {'q': 10, 'w': 80, 'e': 145, 'r': 215, 't': 280, 'y': 440, 'u': 507, 'i': 575, 'o': 641, 'p': 709}
#keys_black = {'q': 10, 'w': 80, 'e': 145, 'r': 215, 't': 280, 'y': 350, 'u': 415}