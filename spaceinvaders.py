#Space Invaders


import turtle
import random
import time






#Screen setup
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)
wn.title("Space Invaders")





#Head setup
wn.register_shape("p.gif")
head1 = turtle.Turtle()
wn.register_shape("p.gif")
head1.shape('p.gif')
head1.penup()
head1.speed(0)
head1.shapesize(2 , 2)
head1.goto(0, -150)


#Bullet setup
bullet = turtle.Turtle()
bullet.color("white")
bullet.penup()
bullet.left(90)
bullet.speed(0)
bullet.shape("square")
bullet.shapesize(0.2, 1)
bullet.ht()


#enemy
wn.register_shape("y.gif")
enemy = turtle.Turtle()
wn.register_shape("y.gif")
enemy.shape('y.gif')
enemy.penup()
enemy.goto(-320, 250)
enemy.color("lime")
enemy.penup()
enemy.speed(0)
enemy.shapesize(1 , 1)

#enemy2
wn.register_shape("y.gif")
enemy2 = turtle.Turtle()
wn.register_shape("y.gif")
enemy2.shape('y.gif')
enemy2.penup()
enemy2.goto(-260, 250)
enemy2.penup()
enemy2.speed(0)
enemy2.shapesize(2 , 2)

#enemy3
wn.register_shape("y.gif")
enemy3 = turtle.Turtle()
wn.register_shape("y.gif")
enemy3.shape('y.gif')
enemy3.penup()
enemy3.goto(-200, 250)
enemy3.penup()
enemy3.speed(0)
enemy3.shapesize(2 , 2)

wn.register_shape("y.gif")
enemy4 = turtle.Turtle()
wn.register_shape("y.gif")
enemy4.shape('y.gif')
enemy4.penup()
enemy4.goto(-140, 250)
enemy4.penup()
enemy4.speed(0)
enemy4.shapesize(2 , 2)

wn.register_shape("y.gif")
enemy5 = turtle.Turtle()
wn.register_shape("y.gif")
enemy5.shape('y.gif')
enemy5.penup()
enemy5.goto(-80, 250)
enemy5.penup()
enemy5.speed(0)
enemy5.shapesize(2 , 2)

#enemy6
wn.register_shape("y.gif")
enemy6 = turtle.Turtle()
wn.register_shape("y.gif")
enemy6.shape('y.gif')
enemy6.penup()
enemy6.goto(-20, 250)
enemy6.penup()
enemy6.speed(0)
enemy6.shapesize(2 , 2)

#enemy7
wn.register_shape("y.gif")
enemy7 = turtle.Turtle()
wn.register_shape("y.gif")
enemy7.shape('y.gif')
enemy7.penup()
enemy7.goto(40, 250)
enemy7.penup()
enemy7.speed(0)
enemy7.shapesize(2 , 2)

#enemy8
wn.register_shape("y.gif")
enemy8 = turtle.Turtle()
wn.register_shape("y.gif")
enemy8.shape('y.gif')
enemy8.penup()
enemy8.goto(100, 250)
enemy8.penup()
enemy8.speed(0)
enemy8.shapesize(2 , 2)

#enemy9
wn.register_shape("y.gif")
enemy9 = turtle.Turtle()
wn.register_shape("y.gif")
enemy9.shape('y.gif')
enemy9.penup()
enemy9.goto(160, 250)
enemy9.penup()
enemy9.speed(0)
enemy9.shapesize(2 , 2)

#enemy10
wn.register_shape("y.gif")
enemy10 = turtle.Turtle()
wn.register_shape("y.gif")
enemy10.shape('y.gif')
enemy10.penup()
enemy10.goto(220, 250)
enemy10.penup()
enemy10.speed(0)
enemy10.shapesize(2 , 2)

#enemy11
wn.register_shape("y.gif")
enemy11 = turtle.Turtle()
wn.register_shape("y.gif")
enemy11.shape('y.gif')
enemy11.penup()
enemy11.goto(280, 250)
enemy11.penup()
enemy11.speed(0)
enemy11.shapesize(2 , 2)


enemy_bullet = turtle.Turtle()
enemy_bullet.penup()
enemy_bullet.ht()
enemy_bullet.color("white")
enemy_bullet.left(90)
enemy_bullet.speed(0)
enemy_bullet.shape("square")
enemy_bullet.shapesize(0.2, 1)
x = enemy.xcor()
y = enemy.ycor()
enemy_bullet.speed(0)
enemy_bullet.goto(x, y)


enemy2_bullet = turtle.Turtle()
enemy2_bullet.penup()
enemy2_bullet.ht()
enemy2_bullet.color("white")
enemy2_bullet.left(90)
enemy2_bullet.speed(0)
enemy2_bullet.shape("square")
enemy2_bullet.shapesize(0.2, 1)
x = enemy2.xcor()
y = enemy2.ycor()
enemy2_bullet.speed(0)
enemy2_bullet.goto(x, y)


enemy3_bullet = turtle.Turtle()
enemy3_bullet.penup()
enemy3_bullet.ht()
enemy3_bullet.color("white")
enemy3_bullet.left(90)
enemy3_bullet.speed(0)
enemy3_bullet.shape("square")
enemy3_bullet.shapesize(0.2, 1)
x = enemy3.xcor()
y = enemy3.ycor()
enemy3_bullet.speed(0)
enemy3_bullet.goto(x, y)


enemy4_bullet = turtle.Turtle()
enemy4_bullet.penup()
enemy4_bullet.ht()
enemy4_bullet.color("white")
enemy4_bullet.left(90)
enemy4_bullet.speed(0)
enemy4_bullet.shape("square")
enemy4_bullet.shapesize(0.2, 1)
x = enemy4.xcor()
y = enemy4.ycor()
enemy4_bullet.speed(0)
enemy4_bullet.goto(x, y)


enemy5_bullet = turtle.Turtle()
enemy5_bullet.penup()
enemy5_bullet.ht()
enemy5_bullet.color("white")
enemy5_bullet.left(90)
enemy5_bullet.speed(0)
enemy5_bullet.shape("square")
enemy5_bullet.shapesize(0.2, 1)
x = enemy.xcor()
y = enemy.ycor()
enemy5_bullet.speed(0)
enemy5_bullet.goto(x, y)


enemy6_bullet = turtle.Turtle()
enemy6_bullet.penup()
enemy6_bullet.ht()
enemy6_bullet.color("white")
enemy6_bullet.left(90)
enemy6_bullet.speed(0)
enemy6_bullet.shape("square")
enemy6_bullet.shapesize(0.2, 1)
x = enemy6.xcor()
y = enemy6.ycor()
enemy6_bullet.speed(0)
enemy6_bullet.goto(x, y)


enemy7_bullet = turtle.Turtle()
enemy7_bullet.penup()
enemy7_bullet.ht()
enemy7_bullet.color("white")
enemy7_bullet.left(90)
enemy7_bullet.speed(0)
enemy7_bullet.shape("square")
enemy7_bullet.shapesize(0.2, 1)
x = enemy7.xcor()
y = enemy7.ycor()
enemy7_bullet.speed(0)
enemy7_bullet.goto(x, y)


enemy8_bullet = turtle.Turtle()
enemy8_bullet.penup()
enemy8_bullet.ht()
enemy8_bullet.color("white")
enemy8_bullet.left(90)
enemy8_bullet.speed(0)
enemy8_bullet.shape("square")
enemy8_bullet.shapesize(0.2, 1)
x = enemy8.xcor()
y = enemy8.ycor()
enemy8_bullet.speed(0)
enemy8_bullet.goto(x, y)

enemy9_bullet = turtle.Turtle()
enemy9_bullet.penup()
enemy9_bullet.ht()
enemy9_bullet.color("white")
enemy9_bullet.left(90)
enemy9_bullet.speed(0)
enemy9_bullet.shape("square")
enemy9_bullet.shapesize(0.2, 1)
x = enemy9.xcor()
y = enemy9.ycor()
enemy9_bullet.speed(0)
enemy9_bullet.goto(x, y)

enemy10_bullet = turtle.Turtle()
enemy10_bullet.penup()
enemy10_bullet.ht()
enemy10_bullet.color("white")
enemy10_bullet.left(90)
enemy10_bullet.speed(0)
enemy10_bullet.shape("square")
enemy10_bullet.shapesize(0.2, 1)
x = enemy10.xcor()
y = enemy10.ycor()
enemy10_bullet.speed(0)
enemy10_bullet.goto(x, y)

enemy11_bullet = turtle.Turtle()
enemy11_bullet.penup()
enemy11_bullet.ht()
enemy11_bullet.color("white")
enemy11_bullet.left(90)
enemy11_bullet.speed(0)
enemy11_bullet.shape("square")
enemy11_bullet.shapesize(0.2, 1)
x = enemy11.xcor()
y = enemy11.ycor()
enemy11_bullet.speed(0)
enemy11_bullet.goto(x, y)
###################################################################

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score: 0 High Score: 0",  align="center", font=("Courier", 24, "normal"))


#################################################################
# Movements for the player
def right():
    x = head1.xcor()
    head1.setx(x + 20)

def left():
    x = head1.xcor()
    head1.setx(x - 20)


def space():
    wn.tracer(1)
    bullet.st()
    x = head1.xcor()
    y = head1.ycor()
    bullet.speed(0)
    bullet.goto(x, y)
    bullet.speed(2)
    y = bullet.ycor()
    bullet.sety(y + 400)
    bullet.ht()


# Keybindings
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(space, "space")


#main game loop

score = 0
high_score = 0


while True:
    wn.update()



    if bullet.xcor() == enemy.xcor():
        if bullet.ycor() >= enemy.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score


    if bullet.xcor() == enemy2.xcor():
        if bullet.ycor() >= enemy2.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score

    if bullet.xcor() == enemy3.xcor():
        if bullet.ycor() >= enemy3.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score

    if bullet.xcor() == enemy4.xcor():
        if bullet.ycor() >= enemy4.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score

    if bullet.xcor() == enemy5.xcor():
        if bullet.ycor() >= enemy5.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score

    if bullet.xcor() == enemy6.xcor():
        if bullet.ycor() >= enemy6.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score

    if bullet.xcor() == enemy7.xcor():
        if bullet.ycor() >= enemy7.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score

    if bullet.xcor() == enemy8.xcor():
        if bullet.ycor() >= enemy8.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score

    if bullet.xcor() == enemy9.xcor():
        if bullet.ycor() >= enemy9.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score


    if bullet.xcor() == enemy10.xcor():
        if bullet.ycor() >= enemy10.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score


    if bullet.xcor() == enemy11.xcor():
        if bullet.ycor() >= enemy11.ycor():

            score += 10
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            if score > high_score:
                high_score = score



    def downs():
        wn.tracer(1)



        y = enemy.ycor()
        enemy.speed(1)
        enemy.sety(y - 20)

        y = enemy2.ycor()
        enemy2.speed(1)
        enemy2.sety(y - 20)

        y = enemy3.ycor()
        enemy3.speed(1)
        enemy3.sety(y - 20)

        y = enemy4.ycor()
        enemy4.speed(1)
        enemy4.sety(y - 20)

        y = enemy5.ycor()
        enemy5.speed(1)
        enemy5.sety(y - 20)

        y = enemy6.ycor()
        enemy6.speed(1)
        enemy6.sety(y - 20)

        y = enemy7.ycor()
        enemy7.speed(1)
        enemy7.sety(y - 20)

        y = enemy8.ycor()
        enemy8.speed(1)
        enemy8.sety(y - 20)

        y = enemy9.ycor()
        enemy9.speed(1)
        enemy9.sety(y - 20)

        y = enemy10.ycor()
        enemy10.speed(1)
        enemy10.sety(y - 20)

        y = enemy11.ycor()
        enemy11.speed(1)
        enemy11.sety(y - 20)


        if bullet.xcor() == enemy.xcor():
            if bullet.ycor() >= enemy.ycor():
                enemy.ht()
                enemy_bullet.ht()
                enemy_bullet.speed(0)
                enemy_bullet.goto(1000, 1000)


                enemy2_bullet.st()
                enemy2_bullet.speed(2)

                y = enemy2_bullet.ycor()
                enemy2_bullet.sety(y - 400)
                enemy2_bullet.ht()


                if enemy2_bullet.xcor() == head1.xcor():
                    if enemy2_bullet.ycor() <= head1.ycor():
                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)
                        enemy2_bullet.ht()
                        x = enemy2.xcor()
                        y = enemy2.ycor()
                        enemy2_bullet.speed(0)
                        enemy2_bullet.goto(x, y)

                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)


                        score = 0
                        pen.clear()
                        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)
                        head1.goto(0, -150)
                        w = turtle.Turtle()
                        w.color("red")
                        w.ht()
                        style = ("Arial", (40), "bold")
                        w.write("Game Over", font = style, align = "center")
                        time.sleep(2)
                        w.clear()
                        head1.st()
                        enemy.st()
                        enemy.speed(0)
                        enemy.goto(-320, 250)
                        enemy2.st()
                        enemy2.speed(0)
                        enemy2.goto(-260, 250)
                        enemy3.st()
                        enemy3.speed(0)
                        enemy3.goto(-200, 250)
                        enemy4.st()
                        enemy4.speed(0)
                        enemy4.goto(-140, 250)
                        enemy5.st()
                        enemy5.speed(0)
                        enemy5.goto(-80, 250)
                        enemy6.st()
                        enemy6.speed(0)
                        enemy6.goto(-20, 250)
                        enemy7.st()
                        enemy7.speed(0)
                        enemy7.goto(40, 250)
                        enemy8.st()
                        enemy8.goto(100, 250)
                        enemy9.st()
                        enemy9.speed(0)
                        enemy9.goto(160, 250)
                        enemy10.st()
                        enemy10.speed(0)
                        enemy10.goto(220, 250)
                        enemy11.st()
                        enemy11.speed(0)
                        enemy11.goto(280, 250)


        if bullet.xcor() == enemy2.xcor():
            if bullet.ycor() >= enemy2.ycor():
                enemy2.ht()
                enemy2_bullet.ht()
                enemy2_bullet.speed(0)
                enemy2_bullet.goto(1000, 1000)



        if bullet.xcor() == enemy3.xcor():
            if bullet.ycor() >= enemy3.ycor():
                enemy3.ht()

                enemy3_bullet.ht()
                enemy3_bullet.speed(0)
                enemy3_bullet.goto(1000, 1000)


                enemy2_bullet.st()
                enemy2_bullet.speed(2)

                y = enemy2_bullet.ycor()
                enemy2_bullet.sety(y - 400)
                enemy2_bullet.ht()

                enemy4_bullet.st()
                enemy4_bullet.speed(2)

                y = enemy4_bullet.ycor()
                enemy4_bullet.sety(y - 400)
                enemy4_bullet.ht()


                if enemy2_bullet.xcor() == head1.xcor() or enemy4_bullet.xcor() == head1.xcor() :
                    if enemy2_bullet.ycor() <= head1.ycor() or enemy4_bullet.ycor() <= head1.ycor():
                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)
                        enemy2_bullet.ht()
                        enemy4_bullet.ht()
                        x = enemy2.xcor()
                        y = enemy2.ycor()
                        enemy2_bullet.speed(0)
                        enemy2_bullet.goto(x, y)
                        x = enemy4.xcor()
                        y = enemy4.ycor()
                        enemy4_bullet.speed(0)
                        enemy4_bullet.goto(x, y)
                        head1.ht()
                        score = 0
                        pen.clear()
                        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)
                        head1.goto(0, -150)
                        w = turtle.Turtle()
                        w.color("red")
                        score = 0
                        high_score = 0
                        w.ht()
                        style = ("Arial", (40), "bold")
                        w.write("Game Over", font = style, align = "center")
                        time.sleep(2)
                        w.clear()
                        head1.st()
                        enemy.st()
                        enemy.speed(0)
                        enemy.goto(-320, 250)
                        enemy2.st()
                        enemy2.speed(0)
                        enemy2.goto(-260, 250)
                        enemy3.st()
                        enemy3.speed(0)
                        enemy3.goto(-200, 250)
                        enemy4.st()
                        enemy4.speed(0)
                        enemy4.goto(-140, 250)
                        enemy5.st()
                        enemy5.speed(0)
                        enemy5.goto(-80, 250)
                        enemy6.st()
                        enemy6.speed(0)
                        enemy6.goto(-20, 250)
                        enemy7.st()
                        enemy7.speed(0)
                        enemy7.goto(40, 250)
                        enemy8.st()
                        enemy8.goto(100, 250)
                        enemy9.st()
                        enemy9.speed(0)
                        enemy9.goto(160, 250)
                        enemy10.st()
                        enemy10.speed(0)
                        enemy10.goto(220, 250)
                        enemy11.st()
                        enemy11.speed(0)
                        enemy11.goto(280, 250)


        if bullet.xcor() == enemy4.xcor():
            if bullet.ycor() >= enemy4.ycor():
                enemy4.ht()
                enemy4_bullet.ht()
                enemy4_bullet.speed(0)
                enemy4_bullet.goto(1000, 1000)

                enemy3_bullet.st()
                enemy3_bullet.speed(2)

                y = enemy3_bullet.ycor()
                enemy3_bullet.sety(y - 400)
                enemy3_bullet.ht()

                enemy6_bullet.st()
                enemy6_bullet.speed(2)

                y = enemy6_bullet.ycor()
                enemy6_bullet.sety(y - 400)
                enemy6_bullet.ht()


                if enemy3_bullet.xcor() == head1.xcor() or enemy3_bullet.xcor() == head1.xcor():
                    if enemy3_bullet.ycor() <= head1.ycor() or enemy6_bullet.ycor() <= head1.ycor():
                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)
                        enemy3_bullet.ht()
                        enemy6_bullet.ht()
                        x = enemy3.xcor()
                        y = enemy3.ycor()
                        enemy3_bullet.speed(0)
                        enemy3_bullet.goto(x, y)
                        x = enemy6.xcor()
                        y = enemy6.ycor()
                        enemy6_bullet.speed(0)
                        enemy6_bullet.goto(x, y)

                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)

                        score = 0
                        pen.clear()
                        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

                        head1.goto(0, -150)
                        w = turtle.Turtle()
                        w.color("red")
                        score = 0
                        high_score = 0
                        w.ht()
                        style = ("Arial", (40), "bold")
                        w.write("Game Over", font = style, align = "center")
                        time.sleep(2)
                        w.clear()
                        head1.st()
                        enemy.st()
                        enemy.speed(0)
                        enemy.goto(-320, 250)
                        enemy2.st()
                        enemy2.speed(0)
                        enemy2.goto(-260, 250)
                        enemy3.st()
                        enemy3.speed(0)
                        enemy3.goto(-200, 250)
                        enemy4.st()
                        enemy4.speed(0)
                        enemy4.goto(-140, 250)
                        enemy5.st()
                        enemy5.speed(0)
                        enemy5.goto(-80, 250)
                        enemy6.st()
                        enemy6.speed(0)
                        enemy6.goto(-20, 250)
                        enemy7.st()
                        enemy7.speed(0)
                        enemy7.goto(40, 250)
                        enemy8.st()
                        enemy8.goto(100, 250)
                        enemy9.st()
                        enemy9.speed(0)
                        enemy9.goto(160, 250)
                        enemy10.st()
                        enemy10.speed(0)
                        enemy10.goto(220, 250)
                        enemy11.st()
                        enemy11.speed(0)
                        enemy11.goto(280, 250)


        if bullet.xcor() == enemy5.xcor():
            if bullet.ycor() >= enemy5.ycor():
                enemy5.ht()

                enemy5_bullet.ht()
                enemy5_bullet.speed(0)
                enemy5_bullet.goto(1000, 1000)


        if bullet.xcor() == enemy6.xcor():
            if bullet.ycor() >= enemy6.ycor():
                enemy6.ht()

                enemy6_bullet.ht()
                enemy6_bullet.speed(0)
                enemy6_bullet.goto(1000, 1000)

                enemy5_bullet.st()
                enemy5_bullet.speed(2)

                y = enemy5_bullet.ycor()
                enemy5_bullet.sety(y - 400)
                enemy5_bullet.ht()

                enemy10_bullet.st()
                enemy10_bullet.speed(2)

                y = enemy10_bullet.ycor()
                enemy10_bullet.sety(y - 400)
                enemy10_bullet.ht()


                if enemy5_bullet.xcor() == head1.xcor() or enemy10_bullet.xcor() == head1.xcor():
                    if enemy5_bullet.ycor() <= head1.ycor() or enemy10_bullet.ycor() <= head1.ycor():
                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)
                        enemy5_bullet.ht()
                        enemy6_bullet.ht()
                        x = enemy5.xcor()
                        y = enemy5.ycor()
                        enemy5_bullet.speed(0)
                        enemy5_bullet.goto(x, y)
                        x = enemy10.xcor()
                        y = enemy10.ycor()
                        enemy10_bullet.speed(0)
                        enemy10_bullet.goto(x, y)

                        head1.ht()
                        x = head1.xcor()
                        y = head1.ycor()
                        bullet.speed(0)
                        bullet.goto(x, y)

                        head1.goto(0, -150)
                        w = turtle.Turtle()
                        w.color("red")

                        score = 0
                        pen.clear()
                        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
                        w.ht()
                        style = ("Arial", (40), "bold")
                        w.write("Game Over", font = style, align = "center")
                        time.sleep(2)
                        w.clear()
                        head1.st()
                        enemy.st()
                        enemy.speed(0)
                        enemy.goto(-320, 250)
                        enemy2.st()
                        enemy2.speed(0)
                        enemy2.goto(-260, 250)
                        enemy3.st()
                        enemy3.speed(0)
                        enemy3.goto(-200, 250)
                        enemy4.st()
                        enemy4.speed(0)
                        enemy4.goto(-140, 250)
                        enemy5.st()
                        enemy5.speed(0)
                        enemy5.goto(-80, 250)
                        enemy6.st()
                        enemy6.speed(0)
                        enemy6.goto(-20, 250)
                        enemy7.st()
                        enemy7.speed(0)
                        enemy7.goto(40, 250)
                        enemy8.st()
                        enemy8.goto(100, 250)
                        enemy9.st()
                        enemy9.speed(0)
                        enemy9.goto(160, 250)
                        enemy10.st()
                        enemy10.speed(0)
                        enemy10.goto(220, 250)
                        enemy11.st()
                        enemy11.speed(0)
                        enemy11.goto(280, 250)


        if bullet.xcor() == enemy7.xcor():
            if bullet.ycor() >= enemy7.ycor():
                enemy7.ht()

                enemy7_bullet.ht()
                enemy7_bullet.speed(0)
                enemy7_bullet.goto(1000, 1000)


        if bullet.xcor() == enemy8.xcor():
            if bullet.ycor() >= enemy8.ycor():
                enemy8.ht()

                enemy8_bullet.ht()
                enemy8_bullet.speed(0)
                enemy8_bullet.goto(1000, 1000)


        if bullet.xcor() == enemy9.xcor():
            if bullet.ycor() >= enemy9.ycor():
                enemy9.ht()

                enemy9_bullet.ht()
                enemy9_bullet.speed(0)
                enemy9_bullet.goto(1000, 1000)


        if bullet.xcor() == enemy10.xcor():
            if bullet.ycor() >= enemy10.ycor():
                enemy10.ht()

                enemy10_bullet.ht()
                enemy10_bullet.speed(0)
                enemy10_bullet.goto(1000, 1000)


        if bullet.xcor() == enemy11.xcor():
            if bullet.ycor() >= enemy11.ycor():
                enemy11.ht()

                enemy11_bullet.ht()
                enemy11_bullet.speed(0)
                enemy11_bullet.goto(1000, 1000)

##################################################################################################################

    downs()

    if head1.xcor()>320 or head1.xcor()<-320 or head1.ycor()>320 or head1.ycor()<-320:
        head1.ht()
        x = head1.xcor()
        y = head1.ycor()
        bullet.speed(0)
        bullet.goto(x, y)

        head1.ht()
        x = head1.xcor()
        y = head1.ycor()
        bullet.speed(0)
        bullet.goto(x, y)
        head1.goto(0, -150)
        w = turtle.Turtle()
        w.color("red")
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        w.ht()
        style = ("Arial", (40), "bold")
        w.write("Game Over", font = style, align = "center")
        time.sleep(2)
        w.clear()
        head1.st()
        enemy.st()
        enemy.speed(0)
        enemy.goto(-320, 250)
        enemy2.st()
        enemy2.speed(0)
        enemy2.goto(-260, 250)
        enemy3.st()
        enemy3.speed(0)
        enemy3.goto(-200, 250)
        enemy4.st()
        enemy4.speed(0)
        enemy4.goto(-140, 250)
        enemy5.st()
        enemy5.speed(0)
        enemy5.goto(-80, 250)
        enemy6.st()
        enemy6.speed(0)
        enemy6.goto(-20, 250)
        enemy7.st()
        enemy7.speed(0)
        enemy7.goto(40, 250)
        enemy8.st()
        enemy8.goto(100, 250)
        enemy9.st()
        enemy9.speed(0)
        enemy9.goto(160, 250)
        enemy10.st()
        enemy10.speed(0)
        enemy10.goto(220, 250)
        enemy11.st()
        enemy11.speed(0)
        enemy11.goto(280, 250)

        x = enemy.xcor()
        y = enemy.ycor()
        enemy_bullet.speed(0)
        enemy_bullet.ht()
        enemy_bullet.goto(x, y)

        x = enemy2.xcor()
        y = enemy2.ycor()
        enemy2_bullet.speed(0)
        enemy2_bullet.ht()
        enemy2_bullet.goto(x, y)

        x = enemy3.xcor()
        y = enemy3.ycor()
        enemy3_bullet.speed(0)
        enemy3_bullet.ht()
        enemy3_bullet.goto(x, y)

        x = enemy4.xcor()
        y = enemy4.ycor()
        enemy4_bullet.speed(0)
        enemy4_bullet.ht()
        enemy4_bullet.goto(x, y)

        x = enemy5.xcor()
        y = enemy5.ycor()
        enemy5_bullet.speed(0)
        enemy5_bullet.ht()
        enemy5_bullet.goto(x, y)

        x = enemy6.xcor()
        y = enemy6.ycor()
        enemy6_bullet.speed(0)
        enemy6_bullet.ht()
        enemy6_bullet.goto(x, y)

        x = enemy7.xcor()
        y = enemy7.ycor()
        enemy7_bullet.speed(0)
        enemy7_bullet.ht()
        enemy7_bullet.goto(x, y)

        x = enemy8.xcor()
        y = enemy8.ycor()
        enemy8_bullet.speed(0)
        enemy8_bullet.ht()
        enemy8_bullet.goto(x, y)

        x = enemy9.xcor()
        y = enemy9.ycor()
        enemy9_bullet.speed(0)
        enemy9_bullet.ht()
        enemy9_bullet.goto(x, y)

        x = enemy10.xcor()
        y = enemy10.ycor()
        enemy10_bullet.speed(0)
        enemy10_bullet.ht()
        enemy10_bullet.goto(x, y)

        x = enemy11.xcor()
        y = enemy11.ycor()
        enemy11_bullet.speed(0)
        enemy11_bullet.ht()
        enemy11_bullet.goto(x, y)



    if head1.xcor() == enemy.xcor():
        if head1.ycor() >= enemy.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            high_score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy2.xcor():
        if head1.ycor() >= enemy2.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)


    if head1.xcor() == enemy3.xcor():
        if head1.ycor() >= enemy3.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy4.xcor():
        if head1.ycor() >= enemy4.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)


    if head1.xcor() == enemy5.xcor():
        if head1.ycor() >= enemy5.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy6.xcor():
        if head1.ycor() >= enemy6.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy7.xcor():
        if head1.ycor() >= enemy7.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy8.xcor():
        if head1.ycor() >= enemy8.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy9.xcor():
        if head1.ycor() >= enemy9.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy10.xcor():
        if head1.ycor() >= enemy10.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

    if head1.xcor() == enemy11.xcor():
        if head1.ycor() >= enemy11.ycor():
            head1.ht()
            x = head1.xcor()
            y = head1.ycor()
            bullet.speed(0)
            bullet.goto(x, y)

            head1.goto(0, -150)
            w = turtle.Turtle()
            w.color("red")
            score = 0
            w.ht()
            style = ("Arial", (40), "bold")
            w.write("Game Over", font = style, align = "center")
            time.sleep(2)
            w.clear()
            head1.st()
            enemy.st()
            enemy.speed(0)
            enemy.goto(-320, 250)
            enemy2.st()
            enemy2.speed(0)
            enemy2.goto(-260, 250)
            enemy3.st()
            enemy3.speed(0)
            enemy3.goto(-200, 250)
            enemy4.st()
            enemy4.speed(0)
            enemy4.goto(-140, 250)
            enemy5.st()
            enemy5.speed(0)
            enemy5.goto(-80, 250)
            enemy6.st()
            enemy6.speed(0)
            enemy6.goto(-20, 250)
            enemy7.st()
            enemy7.speed(0)
            enemy7.goto(40, 250)
            enemy8.st()
            enemy8.goto(100, 250)
            enemy9.st()
            enemy9.speed(0)
            enemy9.goto(160, 250)
            enemy10.st()
            enemy10.speed(0)
            enemy10.goto(220, 250)
            enemy11.st()
            enemy11.speed(0)
            enemy11.goto(280, 250)

###########################################################################

wn.mainloop()
