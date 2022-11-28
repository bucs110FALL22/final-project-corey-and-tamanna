import pygame
import random
class obstacle(pygame.sprite.Sprite):
  def __init__(self,x, y):
    super().__init__()
    self.list = ['Rock1.png', 'Rock2.png', 'shrub_1.png']
    image = random.choice(self.list)
    self.image = pygame.image.load('assets/map_stuff/'+image)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    