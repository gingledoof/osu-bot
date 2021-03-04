# osu-bot
 A bot that can believably play the rythm game, osu!


# Getting Started
1) Download osu! and locate the User folder
2) Extract the contents of User.rar into the User folder
3) Change the following settings: Ignore Beatmap skins and Disable all settings in General


# Using the bot
Begin key tracking by pressing the numlock key. This start key may be changed in utils.py. Refer to pynput documentation.
Stop key tracking by pressing the escape key. This key may be changed in utils.py as well
To adjust the note behavior, create a function and assign it to OsuBot##noteAction.

osu_keys.py is an example implementation
### NOTE: As of right now, the script is stopped when the assigned quit key is pressed.
