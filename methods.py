#Game shiz
import pygame
import random

class Checker():
    def __init__(self):
        pass

    def check_bullet_bot_collision(self,bullets,bots):
        hit = pygame.sprite.groupcollide(bullets,bots,True,True)

    def check_player_bot_collision(self):
        hit = pygame.sprite

    def check_player_edging(self,screen,player): #lmao
        pass #for now
        

class BotHandler():
    def __init__(self,screen,screensize,Bots,bot_group,bot_speed,bot_max_count,spawn_rate):
        self.screen = screen
        self.sw = screensize[0]
        self.sh = screensize[1]

        self.Bots = Bots
        self.bot_group = bot_group
        self.bot_speed = bot_speed
        self.bot_max_count = bot_max_count
        self.spawn_rate = spawn_rate

    def spawn_bot(self,framecount,tps):
        spawn_delay = tps*10//self.spawn_rate
        if framecount % spawn_delay == 0:
            if len(self.bot_group) < self.bot_max_count:
                new_bot = self.Bots(self.screen, self.bot_speed, self.set_spawn())
                self.bot_group.add(new_bot)

    def update_bot(self,player_pos):
        for bot in self.bot_group:
            bot.update(player_pos)
            bot.draw(self.screen)

    '''def set_spawn(self):
        #1.5x rectangle size of screen, spawns ofscreen only
        list_x = [i for i in range(0 - 200 , self.sw + 200) if i not in range(0,self.sw)]
        list_y = [i for i in range(0 - 200, self.sh + 200) if i not in range(0,self.sh)]
        spawn_pos = (random.choice(list_x), random.choice(list_y))
        return spawn_pos'''
    
    def set_spawn(self):
        c1 = random.randint(0,1)
        if c1:
            list_x = [i for i in range(0 - 200 , self.sw + 200) if i not in range(0,self.sw)]
            list_y = [i for i in range(0 - 200, self.sh + 200)]
            spawn_pos = (random.choice(list_x), random.choice(list_y))
            return spawn_pos
        else:
            list_x = [i for i in range(0 - 200 , self.sw + 200)]
            list_y = [i for i in range(0 - 200, self.sh + 200) if i not in range(0,self.sh)]
            spawn_pos = (random.choice(list_x), random.choice(list_y))
            return spawn_pos


        



