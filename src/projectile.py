import pygame
class Projectile(pygame.sprite.Sprite):
  def __init__(self,x = 0, y = 0, direction = 'e'):
    super().__init__()
    size = pygame.display.get_window_size()
    self.width = size[0]
    self.height = size[1]
    self.direction = direction
    self.offset = 10
    self.image = pygame.image.load("assets/bullet.png")
    self.image = pygame.transform.scale(self.image, (10,10))
    self.rect = self.image.get_rect()
    if self.direction == 'e':
      self.rect.x = x+self.offset
      self.rect.y = y
    if self.direction == 's':
      self.rect.x = x
      self.rect.y = y+self.offset
    if self.direction == 'w':
      self.rect.x = x-self.offset
      self.rect.y = y
    if self.direction == 'n':
      self.rect.x = x
      self.rect.y = y-self.offset
    self.speed = 10
    
    
  def update(self):
    if self.direction == 'n':
      self.rect.y -= self.speed
    if self.direction == 'e':
      self.rect.x += self.speed
    if self.direction == 's':
      self.rect.y += self.speed
    if self.direction == 'w':
      self.rect.x -= self.speed
    if self.rect.x < 0 or self.rect.x > self.width:
      self.kill()
    if self.rect.y < 0 or self.rect.y > self.height:
      self.kill()
    


  
    
  