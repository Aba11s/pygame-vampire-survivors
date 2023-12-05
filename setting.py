import pygame

class Global():
    def __init__(self):
        self.SCREENWIDTH = 1300
        self.SCREENHEIGHT = 700
        self.SCREENSIZE = (self.SCREENWIDTH,self.SCREENHEIGHT)

        self.player_pos = (self.SCREENWIDTH//2,self.SCREENHEIGHT//2)
        self.player_speed = 1.5
        self.focus_speed = 1

        self.bullet_speed = 5
        self.bullet_max_count = 30
        self.bullet_haste = 1

        self.bot_spawn_area = (self.SCREENWIDTH*1.5,self.SCREENHEIGHT*1.5)
        self.bot_pos = self.player_pos
        self.bot_speed1 = 1.2
        self.bot_speed2 = 1.4
        self.bot_speed3 = 1.7
        self.bot_max_count = 20
        self.bot_spawn_rate = 7.6

        self.pause = False

    def reset(self):
        #resets all
        pass


class Audio():
    pass