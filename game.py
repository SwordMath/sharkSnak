from random import randint
import time
WIDTH = 1200
HEIGHT = 700
food = Actor("food")
food.pos = 500,270
swordy = Actor("swordy")
swordy.pos = 600,250
mine = Actor("mine")
mine.pos = 30,570
game_over = False
scores = 0
lives = 3
def draw():
    screen.fill("navy")
    swordy.draw()
    mine.draw()
    food.draw()
    screen.draw.text("Score: "+ str(scores)+" Lives: "+str(lives),color="red",topleft=(10,10))

            
def update():
    global scores,lives
    if lives == 0:
        score = open("score.txt","a")
        score.write(str(scores)+" ")
        score.close()
        quit()
    food.x += 5
    mine.x += 5
    if keyboard.up:
        swordy.y -= 6
    if keyboard.down:
        swordy.y += 6
    

    mine_collected = swordy.colliderect(mine)
    food_collected = swordy.colliderect(food)
    if mine_collected:
        lives -= 1
        mine.x = 1
        mine.y = randint(5,750)

    if food_collected:
        scores += 1
        food.x = 5
        food.y = randint(5,750)
    
    if mine.x >= 1200:
        mine.x = 1
        mine.y = randint(5,800)
    if food.x >= 1220: 
        food.x = 1
        food.y = randint(5,800)