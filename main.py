import turtle
import os
import math
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw the border

border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
border_pen.showturtle()

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.pendown()
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.hideturtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.showturtle()

# Player movement
player_speed = 15

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Create the enemy
enemy = turtle.Turtle()
enemy.hideturtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemy.showturtle()

speed = [2, 3, 4, 5]
enemy_speed = random.choice(speed)

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"

# Create the player's bullet
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)

bullet_speed = 20

shot_pen = turtle.Turtle()
shot_pen.penup()
shot_pen.hideturtle()
shot_pen.speed(0)
shot_pen.color("white")
shot_pen.setposition(-200, 350)
shots_string = "Shots: "
shot_pen.write(shots_string, False, align="left", font=("Arial", 18, "normal"))
shots = 0


def fire_bullet():
    global bullet_state, shots, shots_string, shot_pen
    if bullet_state == "ready":
        bullet_state = "fire"
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        shots += 1
        shots_string = "Shots: {}".format(shots)
        shot_pen.clear()
        shot_pen.write(shots_string, False, align="left", font=("Arial", 18, "normal"))

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

score_pen = turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.setposition(150, 350)
score_string = "Score: "
score_pen.write(score_string, False, align="left", font=("Arial", 18, "normal"))
score = 0

# Main game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)
    # Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        enemy_speed *= -1

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        enemy_speed *= -1

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
        bullet.showturtle()

    # Check for bullet collision with enemy
    if isCollision(bullet, enemy):
        # Reset the bullet
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(0, -400)
        # Reset the enemy
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)
        score += 1
        score_string = "Score: {}".format(score)
        score_pen.clear()
        score_pen.write(score_string, False, align="left", font=("Arial", 18, "normal"))

    # Check for collision between enemy and player
    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        final_score_string = "GAME OVER\nFinal Score: {}".format(score)
        score_pen.setposition(0, 0)
        score_pen.write(final_score_string, False, align="center", font=("Arial", 20, "bold"))
        break

    # Check if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

wn.mainloop()

