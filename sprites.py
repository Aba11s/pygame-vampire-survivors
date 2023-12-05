import math
import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self,screen,pos,speed,focus_speed):
        Sprite.__init__(self)
        self.screen = screen

        self.player = pygame.image.load("playertemp.png").convert_alpha()
        self.rect = self.player.get_rect()
        self.rect.center = pos
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

        self.speed = speed
        self.focus = focus_speed
        self.move_left, self.move_right, self.move_up, self.move_down = (False,)*4

        self.invincible = False
        self.shield = False

    def rotate_player(self):
        d_x, d_y = self.m_x - self.rect.x, self.m_y - self.rect.y
        self.dir = (d_x,
                    d_y)

        self.angle = math.degrees(math.atan2(-d_y,d_x)) - 90 #Correction
        self.player_rot = pygame.transform.rotate(self.player, self.angle) 
        self.rect_rot = self.player_rot.get_rect(center = self.rect.center)

    def update(self):
        #Gets mouse pos
        self.m_x, self.m_y = pygame.mouse.get_pos()

        self.rotate_player()

        #Updates movement
        if self.move_up:
            self.centery -= self.speed * self.focus
        if self.move_right:
            self.centerx += self.speed * self.focus
        if self.move_down:
            self.centery += self.speed * self.focus
        if self.move_left:
            self.centerx -= self.speed * self.focus

        self.rect.center = (self.centerx,self.centery)

    def draw(self):
        self.screen.blit(self.player_rot,self.rect_rot.topleft)



class Bullet(Sprite):
    def __init__(self,screen,player_pos,direction,bullet_speed):
        Sprite.__init__(self)
        self.screen = screen
        self.player_pos = player_pos
        self.x = self.player_pos[0]
        self.y = self.player_pos[1]
        self.dir = direction
    
        self.rotate_bullet()
        self.rect = self.bullet.get_rect(center = self.player_pos)
        self.speed = bullet_speed

    def rotate_bullet(self): #not needed for circular bullets
        dist = math.hypot(*self.dir)
        if dist == 0:
            self.dir = (0,-1)
        else:
            self.dir = (self.dir[0]/dist,self.dir[1]/dist)
        angle = math.degrees(math.atan2(-self.dir[1],self.dir[0])) - 90 #Correction

        self.bullet = pygame.Surface((6,6))
        self.bullet.fill("Black")
        self.bullet = pygame.transform.rotate(self.bullet, angle)

    def update(self):
        self.x += self.dir[0] * self.speed
        self.y += self.dir[1] * self.speed
        self.player_pos = (self.x,
                    self.y)
        
        self.rect = self.bullet.get_rect(center = self.player_pos)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"Black",self.rect.center,6,3)



class Bots(Sprite):
    def __init__(self,screen,bot_speed,spawn_pos):
        Sprite.__init__(self)
        self.screen = screen

        self.bot = pygame.Surface((30,30))
        self.rect = self.bot.get_rect(center = spawn_pos)
        self.pos = pygame.math.Vector2(self.rect.topleft) # stores vector as float (IMPORTANT TO PREVENT WEIRD JAGGED MOVEMENT)

        self.speed = bot_speed

    def track_player(self,target_pos): # Player tracking
        self.dirvect = (pygame.math.Vector2(target_pos) - self.pos).normalize()
        self.pos += self.dirvect * self.speed

    def update(self,target_pos):
        self.track_player(target_pos) # Move to player
        self.rect.center = round(self.pos.x),round(self.pos.y)

    def draw(self, screen):
        pygame.draw.circle(screen,"Black",self.rect.center,15,3)






