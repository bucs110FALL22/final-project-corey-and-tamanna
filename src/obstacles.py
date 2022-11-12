import pygame
class player(pygame.sprite.Sprite):
  def __init__(self,x, y):
    super().__init__(self)
    self.image = pygame.image.load("to be named")
    self.rect = self.image.get_rect()