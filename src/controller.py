import pygame
import sys
from src.player import Player
from src.obstacles import Obstacle
from src.projectile import Projectile
import random
class Controller:
  
  def __init__(self, font = 'etc/ARCADECLASSIC.TTF', font_size = 75):
    '''
    sets up and loads all data required to run game
    args: font: str containging font file location, font_size: font size for menu screen
    No return
    '''
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
    self.color_white = (255, 255, 255)
    self.color_red = (255, 0, 0)
  
    self.text_surface1 = self.font.render('Play Game', True, self.color_white)
    self.text_rect1 = self.text_surface1.get_rect()
    self.text_rect1.center = (self.width/2, self.height/6)

    self.text_surface2 = self.font.render('Controls', True, self.color_white)
    self.text_rect2 = self.text_surface2.get_rect()
    self.text_rect2.center = (self.width/2, self.height/2)

    self.text_surface3 = self.font.render('Quit Game', True, self.color_white)
    self.text_rect3 = self.text_surface3.get_rect()       
    self.text_rect3.center = (self.width/2, 5*self.height/6)

    self.menu_text = self.font.render('Main Menu', True, self.color_white)
    self.menu_text_rect = self.menu_text.get_rect()
    self.menu_text_rect.center = (self.width/2, self.height/3)

    self.quit_text = self.text_surface3
    self.quit_text_rect = self.quit_text.get_rect()
    self.quit_text_rect.center = (self.width/2, 2*self.height/3)

    self.arrowwhite = pygame.image.load('assets/whitebackarrow.png')
    self.arrowwhite = pygame.transform.scale(self.arrowwhite, (100, 100))
    self.arrowwhite_rect = self.arrowwhite.get_rect()
    
    
    self.arrowred = pygame.image.load('assets/redbackarrow.png')
    self.arrowred = pygame.transform.scale(self.arrowred, (100, 100))

    self.w_key = pygame.image.load('assets/keyboard/W_White.png')
    self.w_key = pygame.transform.scale(self.w_key, (self.width/9, self.width/9))
    self.w_key_blue = pygame.image.load('assets/keyboard/W_Blue.png')
    self.w_key_blue = pygame.transform.scale(self.w_key_blue, (self.width/9, self.width/9))
    self.w_key_rect = self.w_key.get_rect()
    self.w_key_rect.center = (self.width/6, 7*self.height/9)
    self.w_holder = self.w_key
    
    self.a_key = pygame.image.load('assets/keyboard/A_White.png')
    self.a_key = pygame.transform.scale(self.a_key, (self.width/9, self.width/9))
    self.a_key_blue = pygame.image.load('assets/keyboard/A_Blue.png')
    self.a_key_blue = pygame.transform.scale(self.a_key_blue, (self.width/9, self.width/9))
    self.a_key_rect = self.a_key.get_rect()
    self.a_key_rect.center = (self.width/18, 8*self.height/9)
    self.a_holder = self.a_key

    self.s_key = pygame.image.load('assets/keyboard/S_White.png')
    self.s_key = pygame.transform.scale(self.s_key, (self.width/9, self.width/9))
    self.s_key_blue = pygame.image.load('assets/keyboard/S_Blue.png')
    self.s_key_blue = pygame.transform.scale(self.s_key_blue, (self.width/9, self.width/9))
    self.s_key_rect = self.s_key.get_rect()
    self.s_key_rect.center = (self.width/6, 8*self.height/9)
    self.s_holder = self.s_key
    
    self.d_key = pygame.image.load('assets/keyboard/D_White.png')
    self.d_key = pygame.transform.scale(self.d_key, (self.width/9, self.width/9))
    self.d_key_blue = pygame.image.load('assets/keyboard/D_Blue.png')
    self.d_key_blue = pygame.transform.scale(self.d_key_blue, (self.width/9, self.width/9))
    self.d_key_rect = self.d_key.get_rect()
    self.d_key_rect.center = (5*self.width/18, 8*self.height/9)
    self.d_holder = self.d_key
    
    self.e_key = pygame.image.load('assets/keyboard/E_White.png')
    self.e_key = pygame.transform.scale(self.e_key, (self.width/9, self.width/9))
    self.e_key_blue = pygame.image.load('assets/keyboard/E_Blue.png')
    self.e_key_blue = pygame.transform.scale(self.e_key_blue, (self.width/9, self.width/9))
    self.e_key_rect = self.e_key.get_rect()
    self.e_key_rect.center = (5*self.width/18, 7*self.height/9)
    self.e_holder = self.e_key
    
    self.up_key = pygame.image.load('assets/keyboard/Up_White.png')
    self.up_key = pygame.transform.scale(self.up_key, (self.width/9, self.width/9))
    self.up_key_red = pygame.image.load('assets/keyboard/Up_Red.png')
    self.up_key_red = pygame.transform.scale(self.up_key_red, (self.width/9, self.width/9))
    self.up_key_rect = self.up_key.get_rect()
    self.up_key_rect.center = (15*self.width/18, 7*self.height/9)
    self.up_holder = self.up_key
    
    self.left_key = pygame.image.load('assets/keyboard/Left_White.png')
    self.left_key = pygame.transform.scale(self.left_key, (self.width/9, self.width/9))
    self.left_key_red = pygame.image.load('assets/keyboard/Left_Red.png')
    self.left_key_red = pygame.transform.scale(self.left_key_red, (self.width/9, self.width/9))
    self.left_key_rect = self.left_key.get_rect()
    self.left_key_rect.center = (13*self.width/18, 8*self.height/9)
    self.left_holder = self.left_key

    self.down_key = pygame.image.load('assets/keyboard/Down_White.png')
    self.down_key = pygame.transform.scale(self.down_key, (self.width/9, self.width/9))
    self.down_key_red = pygame.image.load('assets/keyboard/Down_Red.png')
    self.down_key_red = pygame.transform.scale(self.down_key_red, (self.width/9, self.width/9))
    self.down_key_rect = self.down_key.get_rect()
    self.down_key_rect.center = (15*self.width/18, 8*self.height/9)
    self.down_holder = self.down_key

    self.right_key = pygame.image.load('assets/keyboard/Right_White.png')
    self.right_key = pygame.transform.scale(self.right_key, (self.width/9, self.width/9))
    self.right_key_red = pygame.image.load('assets/keyboard/Right_Red.png')
    self.right_key_red = pygame.transform.scale(self.right_key_red, (self.width/9, self.width/9))
    self.right_key_rect = self.right_key.get_rect()
    self.right_key_rect.center = (17*self.width/18, 8*self.height/9)
    self.right_holder = self.right_key

    self.space_key = pygame.image.load('assets/keyboard/SpaceBar_White.png')
    self.space_key = pygame.transform.scale(self.space_key, (self.width/3, self.width/9))
    self.space_key_red = pygame.image.load('assets/keyboard/SpaceBar_Red.png')
    self.space_key_red = pygame.transform.scale(self.space_key_red, (self.width/3, self.width/9))
    self.space_key_rect = self.space_key.get_rect()
    self.space_key_rect.center = (self.width/2, 8*self.height/9)
    self.space_holder = self.space_key

    self.p1_health3 = pygame.image.load('assets/health/p1_health3.png')
    self.p1_health2 = pygame.image.load('assets/health/p1_health2.png')
    self.p1_health1 = pygame.image.load('assets/health/p1_health1.png')
    self.p1_health3 = pygame.transform.scale(self.p1_health3, (3*self.width/13, self.height/16))
    self.p1_health2 = pygame.transform.scale(self.p1_health2, (3*self.width/13, self.height/16))
    self.p1_health1 = pygame.transform.scale(self.p1_health1, (3*self.width/13, self.height/16))
    self.p1_health_rect = self.p1_health1.get_rect()
    self.p1_health_rect.topleft = (0, 0)
    
    self.p2_health3 = pygame.image.load('assets/health/p2_health3.png')
    self.p2_health2 = pygame.image.load('assets/health/p2_health2.png')
    self.p2_health1 = pygame.image.load('assets/health/p2_health1.png')
    self.p2_health3 = pygame.transform.scale(self.p2_health3, (3*self.width/13, self.height/16))
    self.p2_health2 = pygame.transform.scale(self.p2_health2, (3*self.width/13, self.height/16))
    self.p2_health1 = pygame.transform.scale(self.p2_health1, (3*self.width/13, self.height/16))
    self.p2_health_rect = self.p2_health1.get_rect()
    self.p2_health_rect.right = (self.width)
    
    self.controls_text = pygame.image.load('assets/keyboard/Controls_Text.png')
    self.controls_text_rect = self.controls_text.get_rect()
    self.controls_text_rect.center = (self.width/2, self.height/1.5)  
    
    self.p1 = Player(self.width/5, self.height/5, 'blue')
    self.p2 = Player(4*self.width/5, 4*self.height/5, 'red')

    self.num_obs = 5
    self.environment = pygame.sprite.Group()
    for i in range(0, self.num_obs):
      self.environment.add(Obstacle(random.randint(0, self.width-10), (random.randint(0,self.height-10))))

    self.bullet = pygame.sprite.Group()

    myfile = open("assets/data/redwins.txt", "r")
    self.redwins = int(myfile.read())
    myfile.close()

    myfile = open("assets/data/bluewins.txt", "r")
    self.bluewins = int(myfile.read())
    myfile.close()
        
    
    self.STATE = "menu"
  def mainloop(self):
    '''
    main loop of game that handles which sub loop the game is in
    arg: (Controller) self controller
    retruns: (str) with current state
    '''
    while True:
      if self.STATE == 'menu':
        self.menuloop()
      elif self.STATE == 'controls':
        self.controlsloop()
      elif self.STATE== 'game':
        self.gameloop()
      elif self.STATE == 'over':
        self.gameoverloop()
    return self.STATE
  def menuloop(self):
    '''
    loop for the menu state of the game
    args: (Controller) self Controller
    returns: (str) with current state
    '''
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
        self.menu_color1 = self.color_red
      else:
        self.menu_color1 = self.color_white
      if self.text_rect2.collidepoint(pygame.mouse.get_pos()):
        self.menu_color2 = self.color_red
      else:
        self.menu_color2 = self.color_white
      if self.text_rect3.collidepoint(pygame.mouse.get_pos()):
        self.menu_color3 = self.color_red
      else:
        self.menu_color3 = self.color_white
      #update data
      
      #redraw
      self.screen.blit(self.background, (0,0))
      
      self.text_surface1 = self.font.render('Play Game', True, self.menu_color1)
      self.screen.blit(self.text_surface1, self.text_rect1)
      
      self.text_surface2 = self.font.render('Controls', True, self.menu_color2)
      self.screen.blit(self.text_surface2, self.text_rect2)
      
      self.text_surface3 = self.font.render('Quit Game', True, self.menu_color3)
      self.screen.blit(self.text_surface3, self.text_rect3)
      
      pygame.display.update()
    return self.STATE
  def controlsloop(self):
    '''
    loop for the controls state of the game
    args: (Controller) self Controller
    returns: (str) with current state
    '''
    while self.STATE == 'controls':
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_w:
            self.w_holder = self.w_key
          if event.key == pygame.K_a:
            self.a_holder = self.a_key
          if event.key == pygame.K_s:
            self.s_holder = self.s_key
          if event.key == pygame.K_d:
            self.d_holder = self.d_key
          if event.key == pygame.K_e:
            self.e_holder = self.e_key
          if event.key == pygame.K_UP:
            self.up_holder = self.up_key
          if event.key == pygame.K_LEFT:
            self.left_holder = self.left_key
          if event.key == pygame.K_DOWN:
            self.down_holder = self.down_key
          if event.key == pygame.K_RIGHT:
            self.right_holder = self.right_key
          if event.key == pygame.K_SPACE:
            self.space_holder = self.space_key

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            self.w_holder = self.w_key_blue
          if event.key == pygame.K_a:
            self.a_holder = self.a_key_blue
          if event.key == pygame.K_s:
            self.s_holder =  self.s_key_blue
          if event.key == pygame.K_d:
            self.d_holder = self.d_key_blue
          if event.key == pygame.K_e:
            self.e_holder = self.e_key_blue
          if event.key == pygame.K_UP:
            self.up_holder = self.up_key_red
          if event.key == pygame.K_LEFT:
            self.left_holder = self.left_key_red
          if event.key == pygame.K_DOWN:
            self.down_holder = self.down_key_red
          if event.key == pygame.K_RIGHT:
            self.right_holder = self.right_key_red
          if event.key == pygame.K_SPACE:
            self.space_holder =  self.space_key_red
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.arrowwhite_rect.collidepoint(pygame.mouse.get_pos()):
            self.STATE = 'menu'


      
      if self.arrowwhite_rect.collidepoint(pygame.mouse.get_pos()):
        arrow = self.arrowred
      else:
        arrow = self.arrowwhite
      
      self.screen.fill('gray')
      self.screen.blit(arrow, self.arrowwhite_rect)
      self.screen.blit(self.w_holder, self.w_key_rect)
      self.screen.blit(self.a_holder, self.a_key_rect)
      self.screen.blit(self.s_holder, self.s_key_rect)
      self.screen.blit(self.d_holder, self.d_key_rect)
      self.screen.blit(self.e_holder, self.e_key_rect)
      self.screen.blit(self.up_holder, self.up_key_rect)
      self.screen.blit(self.left_holder, self.left_key_rect)
      self.screen.blit(self.right_holder, self.right_key_rect)
      self.screen.blit(self.down_holder, self.down_key_rect)
      self.screen.blit(self.space_holder, self.space_key_rect)
      self.screen.blit(self.controls_text, self.controls_text_rect)
      
      pygame.display.update()
    return self.STATE
  def gameloop(self):
    '''
    loop for the game state of the game
    args: (Controller) self Controller
    returns: (str) with current state'''
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
          if event.key == pygame.K_e:
            self.bullet.add(Projectile(x = self.p1.rect.x, y = self.p1.rect.y, direction = self.p1.direction))
          if event.key == pygame.K_UP:
            self.p2.move_up()
          if event.key == pygame.K_LEFT:
            self.p2.move_left()
          if event.key == pygame.K_RIGHT:
            self.p2.move_right()
          if event.key == pygame.K_DOWN:
            self.p2.move_down()
          if event.key == pygame.K_SPACE:
            self.bullet.add(Projectile(x = self.p2.rect.x, y = self.p2.rect.y, direction = self.p2.direction))
      for bullets in self.bullet:
        if pygame.sprite.collide_rect(self.p1, bullets):
          self.p1.take_damage()
          bullets.kill()
        if pygame.sprite.collide_rect(self.p2, bullets):
          self.p2.take_damage()
          bullets.kill()
      #update data
      if self.p1.health == 3:
        p1_health = self.p1_health3
      if self.p1.health == 2:
        p1_health = self.p1_health2
      if self.p1.health == 1:
        p1_health = self.p1_health1
      if self.p2.health == 3:
        p2_health = self.p2_health3
      if self.p2.health == 2:
        p2_health = self.p2_health2
      if self.p2.health == 1:
        p2_health = self.p2_health1


      if self.p1.health < 1:
        self.p1.reset_health()
        self.p2.reset_health()
        self.bullet.empty()
        myfile = open("assets/data/redwins.txt", "r")
        value = int(myfile.read())
        myfile.close()
        value += 1
        myfile = open("assets/data/redwins.txt", "w")
        myfile.write(str(value))
        myfile.close()
        self.redwins = value
        self.STATE = 'over'
      
      if self.p2.health < 1:
        self.p1.reset_health()
        self.p2.reset_health()
        self.bullet.empty()
        myfile = open("assets/data/bluewins.txt", "r")
        value = int(myfile.read())
        myfile.close()
        value += 1
        myfile = open("assets/data/bluewins.txt", "w")
        myfile.write(str(value))
        myfile.close()
        self.bluewins = value
        self.STATE = 'over'
        
      #redraw

        
      self.screen.blit(self.background, (0,0))
      self.screen.blit(self.p1.image, self.p1.rect)
      self.screen.blit(self.p2.image, self.p2.rect)
      for obs in self.environment:
        self.screen.blit(obs.image, obs.rect)
      for bullets in self.bullet:
        self.screen.blit(bullets.image, bullets.rect)
      self.bullet.update()
      self.screen.blit(p1_health, self.p1_health_rect)
      self.screen.blit(p2_health, self.p2_health_rect)
      pygame.display.update()
    return self.STATE
  
  
  def gameoverloop(self):
    '''
    loop for the gameover state of the game
    args: (Controller) self Controller
    returns: (str) with current state'''
    while self.STATE == 'over':
      #event loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.menu_text_rect.collidepoint(pygame.mouse.get_pos()):
            
            self.STATE = 'menu'
          if self.quit_text_rect.collidepoint(pygame.mouse.get_pos()):
            sys.exit()
      #update data
      if self.menu_text_rect.collidepoint(pygame.mouse.get_pos()):
        self.menu_color1 = self.color_red
      else:
        self.menu_color1 = self.color_white
      if self.quit_text_rect.collidepoint(pygame.mouse.get_pos()):
        self.menu_color2 = self.color_red
      else:
        self.menu_color2 = self.color_white

      self.score = self.font.render(f'Blue Wins {self.bluewins} ||| Red Wins {self.redwins}', True, self.color_white)
      self.score_rect = self.score.get_rect()
      self.score_rect.center = (self.width/2, self.height/12)
      #redraw
      self.screen.fill('black')

      self.menu_text = self.font.render('Main Menu', True, self.menu_color1)
      self.screen.blit(self.menu_text, self.menu_text_rect)
      
      self.quit_text = self.font.render('Quit Game', True, self.menu_color2)
      self.screen.blit(self.quit_text, self.quit_text_rect)
      self.screen.blit(self.score, self.score_rect)
    
      
      pygame.display.update()
    return self.STATE