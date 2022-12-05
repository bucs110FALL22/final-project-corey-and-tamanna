import pygame
class Player(pygame.sprite.Sprite):
  def __init__(self,x=0, y=0, color='blue'):
    '''
    Sets up data needed for Player class
    args: x:gives x chord for player, y: gives y chord for player, color: gives color for player class
    No return
    '''
    super().__init__()
    size = pygame.display.get_window_size()
    self.width = size[0]
    self.height = size[1]
    self.health = 3
    self.direction = 'e'
    self.color = color
    if self.color == 'red':
      self.image = pygame.image.load("assets/character/character_right.png")
    if self.color == 'blue':
      self.image = pygame.image.load("assets/character/character_rightBlue.png")
    self.scale_x = 25
    self.scale_y = 50
    self.image = pygame.transform.scale(self.image, (self.scale_x, self.scale_y))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = 20
    self.color = color
      
  def move_up(self):
    '''
    moves the instance player 1 space up
    args: (Player) self Player
    returns (str) with position and direction
    '''  
    self.rect.y -= self.speed
    if self.rect.y < 0:
      self.rect.y = 0
    self.direction = 'n'
    if self.color == 'red':
      self.image = pygame.image.load("assets/character/character_up.png")
    if self.color == 'blue':
      self.image = pygame.image.load("assets/character/character_upBlue.png")
    self.image = pygame.transform.scale(self.image, (25,50))
    return f'x:{self.rect.x}, y:{self.rect.y}, direction:{self.direction}'
  def move_down(self):
    '''
    moves the instance player 1 space down
    args: (Player) self Player
    returns (str) with position and direction
    '''  
    self.rect.y += self.speed
    if self.rect.y +  self.scale_y > self.height:
      self.rect.y = self.height - self.scale_y
    self.direction = 's'
    if self.color == 'red':
       self.image = pygame.image.load("assets/character/character_down.png")
    if self.color == 'blue':
      self.image = pygame.image.load("assets/character/character_downBlue.png")
    self.image = pygame.transform.scale(self.image, (25,50))
    return f'x:{self.rect.x}, y:{self.rect.y}, direction:{self.direction}'
  def move_right(self):
    '''
    moves the instance player 1 space to the right
    args: (Player) self Player
    returns (str) with position and direction
    '''  
    self.rect.x += self.speed
    if self.rect.x + self.scale_x > self.width:
      self.rect.x = self.width - self.scale_x
    self.direction = 'e'
    if self.color == 'red':
      self.image = pygame.image.load("assets/character/character_right.png")
    if self.color == 'blue':
      self.image = pygame.image.load("assets/character/character_rightBlue.png")
    self.image = pygame.transform.scale(self.image, (25,50))
    return f'x:{self.rect.x}, y:{self.rect.y}, direction:{self.direction}'
  def move_left(self):
    '''
    moves the instance player 1 space to the left
    args: (Player) self Player
    returns (str) with position and direction
    '''
    self.rect.x -= self.speed
    if self.rect.x < 0:
      self.rect.x = 0
    self.direction = 'w'
    if self.color == 'red':
      self.image = pygame.image.load("assets/character/character_left.png")
    if self.color == 'blue':
      self.image = pygame.image.load("assets/character/character_leftBlue.png")
    self.image = pygame.transform.scale(self.image, (25,50))
    return f'x:{self.rect.x}, y:{self.rect.y}, direction:{self.direction}'
  def take_damage(self):
    '''
    reduces instances player health by 1
    args: (Player) self player
    returns (int) of player's current health
    '''
    self.health -= 1
    return self.health
  
  
  def reset_health(self):
    '''
    resets instances player health to 3
    args:(Player) self player
    returns (int) of instances player's health
    '''
    self.health = 3
    return self.health

  def __str__(self):
    '''
    makes return string for general information about instance of player
    arg: (Player) self player
    returns: (str) String of general information about instance of player
    '''
    return_str = f'x:{self.rect.x}, y:{self.rect.y}, direction:{self.direction}, health:{self.health}, color:{self.color}'
    return return_str
    

      
      