###########  Modules  #############
import time
import random
import turtle

##########  Screen  #########
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)
wn.register_shape("invader.gif")
wn.register_shape("player.gif")
wn.title("Space Invaders")
wn.bgpic("space.gif")


########  Characters ############

#player setup
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.goto(0, -200)
player.shapesize(1,1)

## Variables for the enemies  ##
container = []

#### Enemies #######
enemy = turtle.Turtle()
enemy.shape("invader.gif")
enemy.penup()
enemy.shapesize(1, 1)
enemy.setx(-320)
enemy.sety(100)
enemy.dx = 2
enemy.dy = 0
container.append(enemy)

enemy2 = turtle.Turtle()
enemy2.shape("invader.gif")
enemy2.penup()
enemy2.shapesize(1, 1)
enemy2.setx(-220)
enemy2.sety(100)
enemy2.dx = 2
enemy2.dy = 0
container.append(enemy2)

enemy3 = turtle.Turtle()
enemy3.shape("invader.gif")
enemy3.penup()
enemy3.shapesize(1, 1)
enemy3.setx(-120)
enemy3.sety(100)
enemy3.dx = 2
enemy3.dy = 0
container.append(enemy3)

enemy4 = turtle.Turtle()
enemy4.shape("invader.gif")
enemy4.penup()
enemy4.shapesize(1, 1)
enemy4.setx(-20)
enemy4.sety(100)
enemy4.dx = 2
enemy4.dy = 0
container.append(enemy4)

enemy5 = turtle.Turtle()
enemy5.shape("invader.gif")
enemy5.penup()
enemy5.shapesize(1, 1)
enemy5.setx(80)
enemy5.sety(100)
enemy5.dx = 2
enemy5.dy = 0
container.append(enemy5)

enemy6 = turtle.Turtle()
enemy6.shape("invader.gif")
enemy6.penup()
enemy6.shapesize(1, 1)
enemy6.setx(180)
enemy6.sety(100)
enemy6.dx = 2
enemy6.dy = 0
container.append(enemy6)

enemy7 = turtle.Turtle()
enemy7.shape("invader.gif")
enemy7.penup()
enemy7.shapesize(1, 1)
enemy7.setx(280)
enemy7.sety(100)
enemy7.dx = 2
enemy7.dy = 0
container.append(enemy7)

enemy8 = turtle.Turtle()
enemy8.shape("invader.gif")
enemy8.penup()
enemy8.shapesize(1, 1)
enemy8.setx(-320)
enemy8.sety(200)
enemy8.dx = 2
enemy8.dy = 0
container.append(enemy8)

enemy9 = turtle.Turtle()
enemy9.shape("invader.gif")
enemy9.penup()
enemy9.shapesize(1, 1)
enemy9.setx(-220)
enemy9.sety(200)
enemy9.dx = 2
enemy9.dy = 0
container.append(enemy9)

enemy10 = turtle.Turtle()
enemy10.shape("invader.gif")
enemy10.penup()
enemy10.shapesize(1, 1)
enemy10.setx(-120)
enemy10.sety(200)
enemy10.dx = 2
enemy10.dy = 0
container.append(enemy10)

enemy11 = turtle.Turtle()
enemy11.shape("invader.gif")
enemy11.penup()
enemy11.shapesize(1, 1)
enemy11.setx(-20)
enemy11.sety(200)
enemy11.dx = 2
enemy11.dy = 0
container.append(enemy11)

enemy12 = turtle.Turtle()
enemy12.shape("invader.gif")
enemy12.penup()
enemy12.shapesize(1, 1)
enemy12.setx(80)
enemy12.sety(200)
enemy12.dx = 2
enemy12.dy = 0
container.append(enemy12)

enemy13 = turtle.Turtle()
enemy13.shape("invader.gif")
enemy13.penup()
enemy13.shapesize(1, 1)
enemy13.setx(180)
enemy13.sety(200)
enemy13.dx = 2
enemy13.dy = 0
container.append(enemy13)

enemy14 = turtle.Turtle()
enemy14.shape("invader.gif")
enemy14.penup()
enemy14.shapesize(1, 1)
enemy14.setx(280)
enemy14.sety(200)
enemy14.dx = 2
enemy14.dy = 0
container.append(enemy14)

#Bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.penup()
bullet.shapesize(0.5, 0.2)
bullet.shape("square")
p_x = player.xcor()
p_y = player.ycor()
bullet.goto(p_x, p_y)
bullet.ht()
bullet.dx = 0
bullet.dy = 10
bulletstate = "ready"

#Bullet for the enemies
enemy_bullet = turtle.Turtle()
enemy_bullet.color("white")
enemy_bullet.penup()
enemy_bullet.shapesize(0.5, 0.2)
enemy_bullet.shape("square")
enemy_bullet.ht()
enemy_bullet.goto(1000, 1200)
enemy_bullet.dx = 0
enemy_bullet.dy = -20

# Notifications (Game Over, waves)
w = turtle.Turtle()
w.ht()
w.penup()
w.color("red")
w.goto(-220, -100)

#######  Making the scores appear  ########
score = 0
high_score = 0
pen = turtle.Turtle()
pen.ht()
pen.penup()
pen.color("white")
pen.goto(0, 280)
pen.write("Score: {} High score: {} ".format(score, high_score),
          align="center", font=("Courier", 25, "bold"))

####### Keybindings + Movement #########

# Mobing the player to the right
def right():
    x = player.xcor()
    player.setx(x + 20)

# Mobing the player to the left
def left():
    x = player.xcor()
    player.setx(x - 20)

# Moving the bullet upwards
def shoot():
    global bulletstate
    if bulletstate == "ready":
        bullet.st()
        bulletstate = "fire"
        #Moving the bullet up, if the "space" key is pressed
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        shoot.has_been_called = True


######## Enemy shooting ############
def shooting(en):
    enemy_bullet.st()
    x = en.xcor()
    y = en.ycor() - 30
    enemy_bullet.setposition(x, y)

# If the player dies, evertything resets to normal
def reset():

    enemy.setx(-320)
    enemy.sety(100)
    enemy.st()

    enemy2.setx(-220)
    enemy2.sety(100)
    enemy2.st()

    enemy3.setx(-120)
    enemy3.sety(100)
    enemy3.st()

    enemy4.setx(-20)
    enemy4.sety(100)
    enemy4.st()

    enemy5.setx(80)
    enemy5.sety(100)
    enemy5.st()

    enemy6.setx(180)
    enemy6.sety(100)
    enemy6.st()

    enemy7.setx(280)
    enemy7.sety(100)
    enemy7.st()


    enemy8.setx(-320)
    enemy8.sety(200)
    enemy8.st()

    enemy9.setx(-220)
    enemy9.sety(200)
    enemy9.st()

    enemy10.setx(-120)
    enemy10.sety(200)
    enemy10.st()

    enemy11.setx(-20)
    enemy11.sety(200)
    enemy11.st()

    enemy12.setx(80)
    enemy12.sety(200)
    enemy12.st()

    enemy13.setx(180)
    enemy13.sety(200)
    enemy13.st()

    enemy14.setx(280)
    enemy14.sety(200)
    enemy14.st()

    player.goto(0, -200)

    p_x = player.xcor()
    p_y = player.ycor()
    bullet.goto(p_x, p_y)

    bulletstate = "ready"



    
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
if bulletstate == "ready":
    wn.onkeypress(shoot, "space")

########## Declaring variables #########
shoot.has_been_called = False

count = 0

enemies_left = 14

wave = 1

bulletstate = "ready"

#############################  Mainloop  ##################################

while True:

    # Delay on the screen
    time.sleep(0.032)
    
    # updating the screen 
    wn.update()


    #Clearing the "GAME OVER" or the "Wave {} survived" sign
    w.clear()
    w.goto(-130, 100)

    #Moving the bullet up, if the "space" key is pressed
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bullet.dy
        bullet.sety(y)

    #Moving the bullet of the enemies
    y = enemy_bullet.ycor()
    y += enemy_bullet.dy
    enemy_bullet.sety(y)

    # If the player moves out of the screen
    if player.xcor() > 320 or player.xcor() < -320:
        reset()
        score = 0
        pen.clear()
        w.color("red")
        pen.write("Score: {} High score: {} ".format(score, high_score),
                  align="center", font=("Courier", 25, "bold"))
        w.goto(-220, 0)
        w.write("GAME OVER", font=("Courier", 60, "bold"))
        time.sleep(2)
        #Clearing the list, then re-assigning all the enemies for looping
        container = []
        enemies = enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12, enemy13, enemy14
        for ap in enemies:
            container.append(ap)

    # Move the enemies
    for i in container:
        x = i.xcor()
        x += i.dx
        i.setx(x)
        # Increment the counter
        count += 1

        # If the counter divided by 300 has no remainder, (every 5sec (approx)) 
        if count % 300 == 0:
            #Choose a random enemy, and shoot
            r = random.choice(container)
            shooting(r)
            # Move the bullet to the chosen enemy, then make it go down
            y = r.ycor()
            y += enemy_bullet.dy
            enemy_bullet.sety(y)


        # If the bullet hits the player
        if enemy_bullet.distance(player) < 20:
            reset()
            w.goto(-220, 0)
            w.color("red")
            w.write("GAME OVER", font=("Courier", 60, "bold"))
            score = 0
            enemies_left = 14
            wave = 1
            pen.clear()
            pen.write("Score: {} High score: {} ".format(score, high_score),
                      align="center", font=("Courier", 25, "bold"))
            time.sleep(2)
            #Clearing the list, then re-assigning all the enemies for looping
            container = []
            enemies = enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12, enemy13, enemy14
            for ap in enemies:
                container.append(ap)
    
            
        # If the enemies hit the player
        if i.distance(player) < 20:
            reset()
            score = 0
            enemies_left = 14
            wave = 1
            pen.clear()
            w.color("red")
            pen.write("Score: {} High score: {} ".format(score, high_score),
                      align="center", font=("Courier", 25, "bold"))
            w.goto(-220, 0)
            w.write("GAME OVER", font=("Courier", 60, "bold"))
            time.sleep(2)
            #Clearing the list, then re-assigning all the enemies for looping
            container = []
            enemies = enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12, enemy13, enemy14
            for ap in enemies:
                container.append(ap)
    


        # If the bullet reaches the top of the screen, reset its y value
        if bullet.ycor() >= enemy8.ycor():
            y = player.ycor()
            bullet.sety(y)
            bullet.ht()
            bulletstate = "ready"
            shoot.has_been_called = False


        # If the player hits an enemy
        if shoot.has_been_called:
            if bullet.distance(i) < 20:
             i.ht()   
             enemies_left -= 1    
             container.remove(i)  
             bulletstate = "ready"
             #Set the bullet back to the player, once it has hit the enemy
             y = player.ycor()
             bullet.sety(y)
             bullet.ht()
             score += 10
             # If the score ig bigger than the highscore, highscore will equal to the score
             if score > high_score:
                high_score = score
            #Updating the score
             pen.clear()
             pen.write("Score: {} High score: {} ".format(score, high_score),
                       align="center", font=("Courier", 25, "bold"))

        # If there are no enemies left    
        if enemies_left == 0:
            enemies_left = 14
            w.goto(-235, 0)
            w.color("yellow")
            w.write("Wave {} survived".format(wave), font=("Courier", 40, "bold"))
            pen.clear()
            pen.write("Score: {} High score: {} ".format(score, high_score),
                    align="center", font=("Courier", 25, "bold"))
            time.sleep(2)
            reset()
            wave += 1
            #Clearing the list, then re-assigning all the enemies for looping
            container = []
            enemies = enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12, enemy13, enemy14
            for ap in enemies:
                container.append(ap)
            #If the player, has killed all the enemies, the next wave is coming


        # If the enenmies exceed the xcoordinate of 320, lower them down, 
        # and shift them back to  the left side of the screen
        if i.xcor() > 320:
            y = i.ycor()
            y -= 100
            i.sety(y)
            i.setx(-320)

wn.mainloop()
