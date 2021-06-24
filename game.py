from random import randint
import sys
import time
from termcolor import colored
from pygame import mixer
WIDTH = 1200
HEIGHT = 700
trash = Actor("trash")
trash.pos = 38,570
food = Actor("food")
food.pos = 500,270
bluefood = Actor("bluefood")
bluefood.pos = 530,300
swordy = Actor("swordy")
swordy.pos = 600,250
mine = Actor("mine")
mine.pos = 30,570
game_over = False
scores = 0
lives = 5
mixer.init()
mixer.music.load("SharkSwim.mp3")
mixer.music.set_volume(3)
mixer.music.play(loops=500)
message = colored('Ready Player Uno!', 'blue')
print(message)
message = colored('Ready Player Uno!', 'red')
print(message)
message = colored('Ready Player Uno!', 'green')
print(message)
time.sleep(1)
def draw():
    
    screen.fill("navy")
    swordy.draw()
    mine.draw()
    food.draw()
    bluefood.draw()
    trash.draw()
    screen.draw.text("Score: "+ str(scores)+" Hits: "+str(lives),color="red",topleft=(10,10))

            
def update():
    global scores,lives
    if lives == 0:
        
        screen.clear()
        screen.fill("white")
        text = colored('Game Over :( !', 'yellow')
        
        print(text)        
        screen.draw.text(" Game Over"+str(lives),color="red",topleft=(10,10))

        quit()
        
    food.x += 5
    bluefood.x += 5
    mine.x += 5
    trash.x += 5
    if keyboard.up:
        swordy.y -= 6
    if keyboard.down:
        swordy.y += 6
    
    bluefood_yum = swordy.colliderect(bluefood)
    mined = swordy.colliderect(mine)
    food_collected = swordy.colliderect(food)
    trashed = swordy.colliderect(trash)
    if bluefood_yum:
        scores += 2
        bluefood.y = randint(5,750)
        bluefood.x = 5
        print ("YUM")
    if mined:
        lives -= 1
        mine.x = 1
        mine.y = 650
    if trashed:
        lives -= 1
        trash.x = 1 
        trash.y = randint(5,750)
    if food_collected:
        scores += 1
        food.x = 5
        food.y = randint(5,750)
        print ("YUM")
    
    if mine.x >= 1200:
        mine.x = 1
        mine.y = 650
    if food.x >= 1220: 
        food.x = 1
        food.y = randint(5,800)
    if trash.x >= 1220: 
        trash.x = 1
        trash.y = randint(5,800)
    if bluefood.x >= 1220: 
        bluefood.x = 1
        bluefood.y = randint(5,800)
        