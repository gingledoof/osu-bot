# osu-bot
 A bot that can believably play the rythm game, osu!


# Getting Started
1) Download osu! and locate the User folder
2) Extract the contents of User.rar into the User folder
3) Change the following settings: Ignore Beatmap skins and Disable all settings in General


# Using the bot
Begin key tracking by pressing the numlock key. This start key may be changed in utils.py. Refer to pynput documentation.
Stop key tracking by pressing the escape key. This key may be changed in utils.py as well
To adjust the random misses, refer to the getHit function in osu_keys.py. This will be upgraded in a future version
### NOTE: As of right now, every time the bot is restarted using these keys, you MUST restart the python script. This will be resolved in a later fix.
