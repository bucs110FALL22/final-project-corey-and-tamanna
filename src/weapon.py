import pygame
class weapon(pygame.sprite.Sprite):
  def __init__(self,x, y, ammo = 30):
    super().__init__(self)
    self.upgrade = False
    self.ammo = ammo
    self.image = pygame.image.load("to be named")
    self.rect = self.image.get_rect()

  def shoot():
    pass
  