import pygame
class player(pygame.sprite.Sprite):
  def __init__(self,x, y):
    super().__init__(self)
    self.health = 3
    self.direction = 3
    self.inventory = []
    self.image = pygame.image.load("to be named")
    self.rect = self.image.get_rect()
    self.speed = 1

  def move_up(self):
      self.rect.y -= self.speed
        
  def move_down(self):
      self.rect.y += self.speed
        
  def move_right(self):
      self.rect.x += self.speed
        
  def move_left(self):
      self.rect.x -= self.speed
  def aim():
    pass