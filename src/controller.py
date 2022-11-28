import pygame
import sys
from src.player import player
from src.obstacles import obstacle
import random
class Controller:
  
  def __init__(self, font, font_size):
    #setup pygame data
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()
    self.width = size[0]
    self.height = size[1]
    self.background = pygame.image.load("assets/map_stuff/Title_Image.png")
    self.background = pygame.transform.scale(self.background, size)
    self.font_size = font_size
    self.font = font
    self.font = pygame.font.Font(self.font, self.font_size)
    self.menu_color1 = (255, 255, 255)
    self.menu_color2 = (255, 255, 255)
    self.menu_color3 = (255, 255, 255)
    
    self.text_surface1 = self.font.render('Play Game', True, self.menu_color1)
    self.text_rect1 = self.text_surface1.get_rect()
    self.text_rect1.center = (self.width/2, self.height/6)

    self.text_surface2 = self.font.render('Controls', True, self.menu_color2)
    self.text_rect2 = self.text_surface2.get_rect()
    self.text_rect2.center = (self.width/2, self.height/2)

    self.text_surface3 = self.font.render('Quit Game', True, self.menu_color3)
    self.text_rect3 = self.text_surface3.get_rect()       
    self.text_rect3.center = (self.width/2, 5*self.height/6)

    self.arrowwhite = pygame.image.load('assets/whitebackarrow.png')
    self.arrowwhite = pygame.transform.scale(self.arrowwhite, (100, 100))
    self.arrowwhite_rect = self.arrowwhite.get_rect()
    
    
    self.arrowred = pygame.image.load('assets/redbackarrow.png')
    self.arrowred = pygame.transform.scale(self.arrowred, (100, 100))
    
    self.p1 = player(self.width/5, self.height/5, 'blue')
    self.p2 = player(4*self.width/5, 4*self.height/5, 'red')

    self.num_obs = 5
    self.environment = pygame.sprite.Group()
    for i in range(0, self.num_obs):
      self.environment.add(obstacle(random.randint(0, self.width), (random.randint(0,self.height))))
    
    self.STATE = "menu"
  def mainloop(self):
    while True:
      if self.STATE == 'menu':
        self.menuloop()
      elif self.STATE == 'controls':
        self.controlsloop()
      elif self.STATE== 'game':
        self.gameloop()
      elif self.STATE == 'over':
        self.gameoverloop()
  
  def menuloop(self):
    while self.STATE == "menu":
      
      #event loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.text_rect1.collidepoint(pygame.mouse.get_pos()):
            self.STATE = 'game'
          if self.text_rect2.collidepoint(pygame.mouse.get_pos()):
            self.STATE = 'controls'
          if self.text_rect3.collidepoint(pygame.mouse.get_pos()):
            sys.exit()
      if self.text_rect1.collidepoint(pygame.mouse.get_pos()):
        self.menu_color1 = (255, 0, 0)
      else:
        self.menu_color1 = (255, 255, 255)
      if self.text_rect2.collidepoint(pygame.mouse.get_pos()):
        self.menu_color2 = (255, 0, 0)
      else:
        self.menu_color2 = (255, 255, 255)
      if self.text_rect3.collidepoint(pygame.mouse.get_pos()):
        self.menu_color3 = (255, 0, 0)
      else:
        self.menu_color3 = (255, 255, 255)
      #update data
      
      #redraw
      self.screen.fill('aqua marine')
      self.screen.blit(self.background, (0,0))
      
      self.text_surface1 = self.font.render('Play Game', True, self.menu_color1)
      self.screen.blit(self.text_surface1, self.text_rect1)
      
      self.text_surface2 = self.font.render('Controls', True, self.menu_color2)
      self.screen.blit(self.text_surface2, self.text_rect2)
      
      self.text_surface3 = self.font.render('Quit Game', True, self.menu_color3)
      self.screen.blit(self.text_surface3, self.text_rect3)
      
      pygame.display.update()
      
  def controlsloop(self):
    while self.STATE == 'controls':
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.arrowwhite_rect.collidepoint(pygame.mouse.get_pos()):
            self.STATE = 'menu'
      if self.arrowwhite_rect.collidepoint(pygame.mouse.get_pos()):
        arrow = self.arrowred
      else:
        arrow = self.arrowwhite
        
      self.screen.fill('black')
      self.screen.blit(arrow, self.arrowwhite_rect)
      
      
      
      
      pygame.display.update()
  def gameloop(self):
    while self.STATE == 'game': 
    #event loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            self.p1.move_up()
          if event.key == pygame.K_a:
            self.p1.move_left()
          if event.key == pygame.K_d:
            self.p1.move_right()
          if event.key == pygame.K_s:
            self.p1.move_down()
          if event.key == pygame.K_UP:
            self.p2.move_up()
          if event.key == pygame.K_LEFT:
            self.p2.move_left()
          if event.key == pygame.K_RIGHT:
            self.p2.move_right()
          if event.key == pygame.K_DOWN:
            self.p2.move_down()
            
          
          
      #update data

      #redraw
      self.screen.fill('aqua marine')
      self.screen.blit(self.background, (0,0))
      self.screen.blit(self.p1.image, self.p1.rect)
      self.screen.blit(self.p2.image, self.p2.rect)
      for obs in self.environment:
        self.screen.blit(obs.image, obs.rect)
      pygame.display.update()
  def gameoverloop(self):
    while self.STATE == 'over':
      #event loop
      pass
      #update data

      #redraw
