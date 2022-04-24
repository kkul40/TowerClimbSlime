import pygame

class Slime():
    def __init__(self,win, win_res):
        self.win = win
        self.win_res = win_res
        self.slime_idle = pygame.image.load("Assets/Slime-idle.png")
        self.slime_idle = pygame.transform.scale(self.slime_idle, (32,32))
        self.slime_idle_right = pygame.transform.flip(self.slime_idle, True, False)

        self.width = self.slime_idle.get_width()
        self.height = self.slime_idle.get_height()
        self.rect = pygame.Rect(250-self.slime_idle.get_width()/2, 900- self.height, self.width, self.height)

        self.gravity = 0.7
        self.gravity_vel = 0
        self.yer_kaldır = True

        self.x_vel_max = 10
        self.x_vel = 0
        self.left = False
        self.right = False
        self.is_jump = True
        self.jump_vel = 11
        self.l_dir = False

    def update(self, list , kamera_vel):
        self.list = list
        self.is_jump = True

        # HARKET ETTİRME
        if self.left:
            if self.x_vel > 0:
                self.x_vel -= 1
            else:
                self.x_vel -= 0.5
            self.l_dir = False
        elif self.right:
            if self.x_vel < 0:
                self.x_vel += 1
            else:
                self.x_vel += 0.5
            self.l_dir = True
        else:
            if self.x_vel > 0.5:
                self.x_vel -= 1
            elif self.x_vel < -0.5:
                self.x_vel += 1
            else:
                self.x_vel = 0

        if abs(self.x_vel) > abs(self.x_vel_max):
            if self.x_vel > abs(self.x_vel_max):
                isaret = 1
            else:
                isaret = -1
            self.x_vel = self.x_vel_max*isaret

        # YER ÇEKİMİ
        self.gravity_vel += self.gravity
        
        for x in self.list:
            if self.gravity_vel > 0:
                if x.rect.colliderect(self.rect.x, self.rect.y + self.gravity_vel, self.width, self.height):
                    if x.rect.top - self.rect.bottom + self.gravity_vel >= 0:
                        self.rect.bottom = x.rect.top
                        self.gravity_vel = x.vel
                        self.is_jump = False

        # KENARLARA ÇARPMA ALGILAMA
        if self.rect.left < 0:
            self.rect.left = 0
            self.x_vel /= -1.2
        elif self.rect.right > self.win_res[0]:
            self.rect.right = 500
            self.x_vel /= -1.2

        if self.yer_kaldır:    
            if self.rect.bottom + self.gravity_vel >= self.win_res[1]:
                self.rect.bottom = self.win_res[1]
                self.gravity_vel = 0
                self.is_jump = False

        self.rect.x += self.x_vel
        self.rect.y += self.gravity_vel + kamera_vel

        self.draw()
    
    def collide(self):
        self.is_jump = False

    def draw(self):
        if self.x_vel > 0:
            self.l_dir = True
        elif self.x_vel < 0:
            self.l_dir = False

        if self.l_dir:
            self.win.blit(self.slime_idle_right, (self.rect.x, self.rect.y))   
        else:
            self.win.blit(self.slime_idle, (self.rect.x, self.rect.y))   
        
        pygame.draw.rect(self.win,(255,0,0), self.rect,1)