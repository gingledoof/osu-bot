from OsuBot import OsuBot
from random import randint

#custom note behavior
def noteAction(bot, key):
    if (bot.combo < 2000 and randint(1, 20) == 2) or randint(1, 1000) > 5:
        bot.combo += 1
        bot.cont.press(key)
    else:
        # Note miss, combo break
        bot.combo = 0

bot = OsuBot(mode='10k') #Setting mode to 10 key mode
#bot.noteAction = noteAction #Setting behavior function. Add this line to allow custom function






