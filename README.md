:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Multi-Player Multi-Wars
## CS 110 Final Project
### S1, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

(https://replit.com/join/eahmnqexrn-coreysammataro1)

<< [link to demo presentation slides](#) >>

### Team: Corey and Tamanna
#### << Team Members >>
Corey and Tamanna

***

## Project Description

<< Give an overview of your project >>
Our game is a simple 1 v 1 game where the goal is to shoot your opponent 3 times. There is also a main menu screen, as well as an interactive controls screen to help players understand how to play.
***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>

    etc/Readmeimages/Gui_early.png
      This was the only thing we had when we initialy started and created the rest as it came up.
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

*** etc/Readmeimages/mainmenu.png
    etc/Readmeimages/controls.png
    etc/Readmeimages/gamescreen.png
    etc/Readmeimages/gameoverscreen.png

    
## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg)

        etc/Readmeimages/Classdesigndiagram.jpg

* Classes
    * << You should have a list of each of your classes with a description. >>
    Controller
      initialized and manages the game loops
    Obstacle
      initializes the obstacle objects. It picks a random image file and places it at random cordanates on the game screen.
    Player
      initializes the players and dirrect them how to move and shoot
    Projectile
      initializes the projectiles and dirrects them how to move across the screen
## Project Structure and File List ***

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
    * controller.py
    * obstacles.py
    * player.py
    * projectile.py
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
    * character (folder)
      * charcter up/down/right/left for blue and red
    * health (folder)
      * health bar level 1-3 for both blue and red
    * keyboard (folder)
      * white and colored images of keys used on controlls screen
    * map_stuff (folder)
      * includes the background image as well images for obstacle class
    * bullet.png
      * image for bullet class
    * (red/white)arrow.png
      * images for red and white arrow respectivly used for back arrows
    * data folder
      * This folder holds txt files for the total number of wins for blue and red

* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>
    * ARCADECLASSIC.TFF
      * (IDK if this goes here) The font used for texts in the code
    * readmeimages folder
      * as folders for images needed for read 

***

## Tasks and Responsibilities ***

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.
   * Corey Sammataro has programmed majority of the software and implemented a graphical user interface in the game.
   * Tamanna Arora has written the proposal, API, Readme and the ATP included in it.

## Testing

The code was regularly tested upon making any updates in the controller class and while designing the GUI. 
Furthermore, we had friends test the game to make sure we accounted for different play styles.

## ATP


  etc/Readmeimages/CS110 ATP1024_1.jpg
  

           	

![image](image.png)
