import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

TITLE = 'bee game: )'

score = 0 
game_over = False

bee = Actor('bee')
bee.pos = 100,100

flower = Actor('flower')
flower.pos = 200,200

def draw():
    screen.blit('bg',(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: " + str(score), color='black', topleft=(10,10))



pgzrun.go()