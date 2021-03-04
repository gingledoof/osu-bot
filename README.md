# osu-bot
A bot that can believably play the rythm game, osu!
 
NOTE: Only can play osu!mania as of right now.


# Getting Started
1) Download osu! and locate the User folder
2) Extract the contents of User.rar into the User folder
3) Change the following settings: Ignore Beatmap skins, Unlimited Frame Rate, and disable all settings in General
4) Set monitor to 1980x1080, as this is the only resolution that currently works.


# Using the bot
Begin key tracking by pressing the numlock key. This start key may be changed when instantiating OsuBot object. Refer to OsuBot and pynput documentation.
Stop key tracking by pressing the escape key. This key may be changed as well
To adjust the note behavior, create a function and assign it to OsuBot##noteAction.

osu_keys.py is an example implementation
### NOTES:
As of right now, the script is stopped when the assigned quit key is pressed. You may encounter issues if your computer is running slow while using this bot, as it is heavily reliant on accurate framerates
