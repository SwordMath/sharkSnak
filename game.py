from random import randint
import sys
import time
from termcolor import colored
WIDTH = 1200
HEIGHT = 700
trash = Actor("trash")
trash.pos = 38,570
food = Actor("food")
food.pos = 500,270
swordy = Actor("swordy")
swordy.pos = 600,250
mine = Actor("mine")
mine.pos = 30,570
game_over = False
scores = 0
lives = 5


def draw():
    screen.fill("navy")
    swordy.draw()
    mine.draw()
    food.draw()
    trash.draw()
    screen.draw.text("Score: "+ str(scores)+" Hits: "+str(lives),color="red",topleft=(10,10))

            
def update():
    global scores,lives
    if lives == 0:
        
        screen.clear
        screen.fill("white")
        text = colored('Game Over :( !', 'yellow')
        print(text)        
        quit()
        
    food.x += 5
    mine.x += 5
    trash.x += 5
    if keyboard.up:
        swordy.y -= 6
    if keyboard.down:
        swordy.y += 6
    

    mined = swordy.colliderect(mine)
    food_collected = swordy.colliderect(food)
    trashed = swordy.colliderect(trash)
    if mined:
        lives -= 1
        mine.x = 1
        mine.y = randint(5,30)
    if trashed:
        lives -= 1
        trash.x = 1 
        trash.y = randint(5,750)
    if food_collected:
        scores += 1
        food.x = 5
        food.y = randint(5,750)
    
    if mine.x >= 1200:
        mine.x = 1
        mine.y = randint(5,30)
    if food.x >= 1220: 
        food.x = 1
        food.y = randint(5,800)
    if trash.x >= 1220: 
        trash.x = 1
        trash.y = randint(5,800)