import pygame
import random
class Obstacle(pygame.sprite.Sprite):
  def __init__(self,x = 0, y=0):
    '''
    sets up data needed for obstacle class
    args: x: gives x chord for obstacle, y:gives y chord for obstacle
    No return
    '''
    super().__init__()
    self.list = ['Rock1.png', 'Rock2.png', 'shrub_1.png', 'tree_2.png']
    self.image_chosen = random.choice(self.list)
    self.image = pygame.image.load('assets/map_stuff/'+ self.image_chosen)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  def __str__(self):
    '''
    makes return string for general information about instance of Obstacle
    arg: (Obstacle) self Obstacle
    returns: (Str) of general information about instance of Obstacle
    '''
    return_str = f'x:{self.rect.x}, y:{self.rect.y}, image:{self.image_chosen}'
    return return_str