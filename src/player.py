import pygame
class player(pygame.sprite.Sprite):
  def __init__(self,x, y, color):
    super().__init__()
    size = pygame.display.get_window_size()
    self.width = size[0]
    self.height = size[1]
    self.health = 3
    self.direction = 3
    self.color = color
    if self.color == 'red':
      self.image = pygame.image.load("assets/character/character_right.png")
    if self.color == 'blue':
      self.image = pygame.image.load("assets/character/character_rightBlue.png")
    self.image = pygame.transform.scale(self.image, (25,50))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = 15
    self.color = color
      
  def move_up(self):
      self.rect.y -= self.speed
      if self.rect.y < 0:
        self.rect.y = 0
      self.direction = 'n'
      if self.color == 'red':
        self.image = pygame.image.load("assets/character/character_up.png")
      if self.color == 'blue':
        self.image = pygame.image.load("assets/character/character_upBlue.png")
      self.image = pygame.transform.scale(self.image, (25,50))
  def move_down(self):
      self.rect.y += self.speed
      if self.rect.y > self.height:
        self.rect.y = self.height
      self.direction = 's'
      if self.color == 'red':
        self.image = pygame.image.load("assets/character/character_down.png")
      if self.color == 'blue':
        self.image = pygame.image.load("assets/character/character_downBlue.png")
      self.image = pygame.transform.scale(self.image, (25,50))
  def move_right(self):
      self.rect.x += self.speed
      if self.rect.x > self.width:
        self.rect.x = self.width
      self.direction = 'e'
      if self.color == 'red':
        self.image = pygame.image.load("assets/character/character_right.png")
      if self.color == 'blue':
        self.image = pygame.image.load("assets/character/character_rightBlue.png")
      self.image = pygame.transform.scale(self.image, (25,50))
  def move_left(self):
      self.rect.x -= self.speed
      if self.rect.x < 0:
        self.rect.x = 0
      self.direction = 'w'
      if self.color == 'red':
        self.image = pygame.image.load("assets/character/character_left.png")
      if self.color == 'blue':
        self.image = pygame.image.load("assets/character/character_leftBlue.png")
      self.image = pygame.transform.scale(self.image, (25,50))
  def take_damage(self):
    self.health -= 1

