import pygame
import src.controller
def main():
  pygame.init()
  controller = src.controller.Controller(font = 'etc/ARCADECLASSIC.TTF', font_size = 75)
  controller.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
