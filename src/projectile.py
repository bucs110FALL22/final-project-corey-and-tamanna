import pygame
class Projectile(pygame.sprite.Sprite):
  def __init__(self,x = 0, y = 0, direction = 'e'):
    '''
    Sets up data needed for Projectile class
    args: x:gives x chord for projectile, y: gives y chord for projectile, direction: gives direction for bullet
    No return
    '''
    super().__init__()
    size = pygame.display.get_window_size()
    self.width = size[0]
    self.height = size[1]
    self.direction = direction
    self.offset = 30
    self.image = pygame.image.load("assets/bullet.png")
    self.image = pygame.transform.scale(self.image, (10,10))
    self.rect = self.image.get_rect()
    if self.direction == 'e':
      self.rect.x = x+ 2*self.offset
      self.rect.y = y
    if self.direction == 's':
      self.rect.x = x
      self.rect.y = y + 2*self.offset
    if self.direction == 'w':
      self.rect.x = x-self.offset
      self.rect.y = y
    if self.direction == 'n':
      self.rect.x = x
      self.rect.y = y-self.offset
    self.speed = 10
    
    
  def update(self):
    '''
    updates the bullets position on the screen, and checks if the bullet as left the screen. If so it is removed from the group and no longer updated.
    args: (Projectile): self projectile 
    returns: (str) returns the direction as a string letter
    '''
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
    return self.direction

  def __str__(self):
    '''
    makes return string for general information about instance of bullet
    arg: (Projectile) self projectile
    returns: (str) String of general information about instance of bullet
    '''
    return_str = f'direction:{self.direction}, x:{self.rect.x}, y:{self.rect.y}'
    return return_str