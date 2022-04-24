import pygame

class Platform():
    def __init__(self, win, win_res, pos_x, pos_y):
        
        
        """ pygame.draw.rect(ekran, (255,0,0), (0,0,200,40))
            pygame.draw.rect(ekran, (255,0,0), (0,100,300,40))
            pygame.draw.rect(ekran, (255,0,0), (0,200,130,40))
            pygame.draw.rect(ekran, (255,0,0), (0,300,500,40))
        """

        self.win = win
        self.win_res = win_res
        self.vel = 0
        self.rect = pygame.Rect(pos_x, pos_y, 100, 30)

    def update(self, kamera_vel):
        self.rect.y += self.vel + kamera_vel
        pygame.draw.rect(self.win, (200,200,200), self.rect)
        
    def setVel(self, deger):
        self.vel = deger