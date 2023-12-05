import pygame
import math
import sys

from setting import Global
from sprites import Player, Bullet, Bots
from methods import Checker, BotHandler as BH

#main

class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.tps = 120
        self.gs = Global()
        self.fire = False
        self.frame_count = 0

        self.screen = pygame.display.set_mode((self.gs.SCREENWIDTH,self.gs.SCREENHEIGHT))
        self.srf = pygame.surface.Surface((self.gs.SCREENWIDTH,self.gs.SCREENHEIGHT))
        self.running = True

        self.load_all()

    def load_all(self):
        #Sprite Groups
        self.bullets = pygame.sprite.Group()
        self.bots_1 = pygame.sprite.Group()
        self.bots_2 = pygame.sprite.Group()

        #Sprite objects
        self.player = Player(self.screen,self.gs.player_pos,self.gs.player_speed,self.gs.focus_speed)

        #Game checkers
        self.col = Checker()
        self.bh = BH(self.screen, self.gs.SCREENSIZE, Bots, self.bots_1,
                      self.gs.bot_speed1, self.gs.bot_max_count, self.gs.bot_spawn_rate)

    def check_key_downs(self,event):
        if event.key == pygame.K_ESCAPE:
            if self.gs.pause == False:
                self.gs.pause = True
            else:
                self.gs.pause = False

        if event.key == pygame.K_d:
            self.player.move_right = True
        if event.key == pygame.K_a:
            self.player.move_left = True
        if event.key == pygame.K_s:
            self.player.move_down = True
        if event.key == pygame.K_w:
            self.player.move_up = True

    def check_key_ups(self,event):
        if event.key == pygame.K_d:
            self.player.move_right = False
        if event.key == pygame.K_a:
            self.player.move_left = False
        if event.key == pygame.K_s:
            self.player.move_down = False
        if event.key == pygame.K_w:
            self.player.move_up = False

    def check_mouse_downs(self,event):
        if event.button == 1:
            self.fire = True

    def check_mouse_ups(self,event):
        if event.button == 1:
            self.fire = False

    def fire_bullet(self):
        if len(self.bullets) < self.gs.bullet_max_count:
            new_bullet = Bullet(self.screen, self.player.rect.center, self.player.dir, self.gs.bullet_speed)
            self.bullets.add(new_bullet)

    def update_screen(self):
        self.srf.fill("Yellow")
        self.screen.blit(self.srf,(0,0))

        self.player.update()
        self.player.draw()

        if self.fire == True:
            if self.frame_count % 20 == 0:
                self.fire_bullet()

        for bullet in self.bullets:
            bullet.update()
            if not self.screen.get_rect().collidepoint(bullet.player_pos):
                self.bullets.remove(bullet)
                
        for bullet in self.bullets:
            bullet.draw(self.screen)

        '''if self.frame_count % 120 == 0:
            self.bh.spawn_bot()'''

        '''for bot in self.bots_1:
            bot.update((self.player.rect.centerx, self.player.rect.centery))

        for bot in self.bots_1:
            bot.draw(self.screen)'''
        
        self.bh.spawn_bot(self.frame_count,self.tps)
        self.bh.update_bot((self.player.centerx,self.player.centery))

        self.col.check_bullet_bot_collision(self.bullets,self.bots_1)
    
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.check_key_downs(event)
                if event.type == pygame.KEYUP:
                    self.check_key_ups(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_mouse_downs(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.check_mouse_ups(event)
            
            self.update_screen()
            self.frame_count += 1
            self.clock.tick(self.tps)
            pygame.display.flip()



if __name__ == '__main__':
    main = Main()
    main.run()