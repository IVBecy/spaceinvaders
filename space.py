# Modules
import time,random,turtle

# Variables
score = 0
high_score = 0
shoot_called = False
count = 0
wave = 1
bulletstate = "ready"

# Class for screen setup
class Screen():
  def __init__(self):
    # screen
    self.wn = turtle.Screen()
    self.wn.bgcolor("black")
    self.wn.setup(width=700, height=700)
    self.wn.tracer(False)
    self.wn.register_shape("images/invader.gif")
    self.wn.register_shape("images/player.gif")
    self.wn.title("Space Invaders")
    self.wn.bgpic("images/space.gif")
    # player
    self.player = turtle.Turtle()
    self.player.shape("images/player.gif")
    self.player.penup()
    self.player.speed(0)
    self.player.goto(0, -200)
    self.player.shapesize(1, 1)
    # array for enemies
    self.container = []
    # bullet
    self.bullet = turtle.Turtle()
    self.bullet.color("white")
    self.bullet.penup()
    self.bullet.shapesize(0.5, 0.2)
    self.bullet.shape("square")
    p_x = self.player.xcor()
    p_y = self.player.ycor()
    self.bullet.goto(p_x, p_y)
    self.bullet.ht()
    self.bullet.dx = 0
    self.bullet.dy = 10
    # bullet for the enemies
    self.enemy_bullet = turtle.Turtle()
    self.enemy_bullet.color("white")
    self.enemy_bullet.penup()
    self.enemy_bullet.shapesize(0.5, 0.2)
    self.enemy_bullet.shape("square")
    self.enemy_bullet.ht()
    self.enemy_bullet.goto(1000, 1200)
    self.enemy_bullet.dx = 0
    self.enemy_bullet.dy = -20
    # notifications
    self.notification = turtle.Turtle()
    self.notification.ht()
    self.notification.penup()
    self.notification.color("red")
    self.notification.goto(-220, -100)
    # score counter
    self.pen = turtle.Turtle()
    self.pen.ht()
    self.pen.penup()
    self.pen.color("white")
    self.pen.goto(0, 280)
    self.pen.write(f"Score: {score} High score: {high_score} ",align="center", font=("Courier", 25, "bold"))
    # make the enemies
    self.make_enemies(-320, 100)
    self.make_enemies(-320, 200)

  # For making enemies appear on the screen
  def make_enemies(self,start_x,start_y):
    for i in range(7):
      self.e = turtle.Turtle()
      self.e.shape("images/invader.gif")
      self.e.penup()
      self.e.shapesize(1, 1)
      self.e.setx(start_x)
      self.e.sety(start_y)
      self.e.dx = 2
      self.e.dy = 0
      self.container.append(self.e)
      # set different position
      start_x += 100

# Keybindings and movements
class Movements():
  # vars
  def __init__(self,player,bullet,enemy_bullet):
    self.player = player
    self.bullet = bullet
    self.enemy_bullet = enemy_bullet

  # moving right
  def right(self):
    x = self.player.xcor()
    self.player.setx(x + 20)

  # moving left
  def left(self):
    x = self.player.xcor()
    self.player.setx(x - 20)

  # shooting
  def shoot(self):
    global bulletstate,shoot_called
    if bulletstate == "ready":
        self.bullet.st()
        bulletstate = "fire"
        x = self.player.xcor()
        y = self.player.ycor() + 10
        self.bullet.setposition(x, y)
        shoot_called = True
        return shoot_called,self.bullet,self.player

  # enemy shooting
  def enemy_shoot(self,enemy):
      self.enemy_bullet.st()
      x = enemy.xcor()
      y = enemy.ycor() - 30
      self.enemy_bullet.setposition(x, y)
      return self.enemy_bullet
      
# Make the screen
s = Screen()
# Movements
m = Movements(s.player, s.bullet, s.enemy_bullet)
s.wn.listen()
s.wn.onkeypress(m.left, "Left")
s.wn.onkeypress(m.right, "Right")
s.wn.onkeypress(m.shoot, "space")
enemies_left = len(s.container)

# Reset on game over
def reset():
  global enemies_left
  s.pen.clear()
  s.pen.write(f"Score: {score} High score: {score} ",align="center", font=("Courier", 25, "bold"))
  s.player.goto(0, -220)
  for i in s.container:
    i.ht()
  s.container = []
  s.make_enemies(-320, 100)
  s.make_enemies(-320, 200)
  enemies_left = len(s.container)
  time.sleep(2)

# For gameover
def game_over():
  global score,wave
  score = 0
  wave = 1
  s.notification.color("red")
  s.notification.goto(-220, 0)
  s.notification.write("GAME OVER", font=("Courier", 60, "bold"))
  reset()
  s.notification.clear()
  s.notification.goto(1000, 1000)

def logic():
  global bulletstate,count,wave,shoot_called,enemies_left,score,high_score

  # Delay
  time.sleep(0.03)

  # Update screen
  s.wn.update()

  # Moving enemy bullets
  y = s.enemy_bullet.ycor()
  y += s.enemy_bullet.dy
  s.enemy_bullet.sety(y)

  # Moving the bullet up when shooting
  if bulletstate == "fire":
    y = s.bullet.ycor()
    y += s.bullet.dy
    s.bullet.sety(y)

  # Moving the enemies
  for i in s.container:
    x = i.xcor()
    x += i.dx
    i.setx(x)
    count += 1

    # Lower enemies
    if i.xcor() > 320:
      y = i.ycor()
      y -= 100
      i.sety(y)
      i.setx(-320)

    # Enemy shooting
    if count % 300 == 0:
      r = random.choice(s.container)
      m.enemy_shoot(r)
      y = r.ycor()
      y += s.enemy_bullet.dy
      s.enemy_bullet.sety(y)

    # If the player's bullet hits an enemy
    if shoot_called:
      if s.bullet.distance(i) <= 20:
        i.ht()
        s.container.remove(i)
        enemies_left -= 1
        bulletstate = "ready"
        y = s.player.ycor()
        s.bullet.sety(y)
        s.bullet.ht()
        score += 10
        if score > high_score:
          high_score = score
        s.pen.clear()
        s.pen.write(f"Score: {score} High score: {high_score} ",align="center", font=("Courier", 25, "bold"))

    if s.enemy_bullet.distance(s.player) <= 20:
      game_over()

    # If the enemies hit the player
    if i.distance(s.player) <= 20:
      game_over()

  # Stop the player's bullet where the last player is
  if len(s.container) > 0:
    if s.bullet.ycor() >= s.container[-1].ycor():
        y = s.player.ycor()
        s.bullet.sety(y)
        s.bullet.ht()
        bulletstate = "ready"
        shoot_called = False

  # If the player goes out of screen
  if s.player.xcor() > 320 or s.player.xcor() < -320:
    game_over()

  # If there are no enemies left
  if enemies_left == 0:
    s.notification.color("yellow")
    s.notification.goto(-235, 0)
    s.notification.write(f"Wave {wave} survived!", font=("Courier", 40, "bold"))
    reset()
    s.notification.clear()
    s.notification.goto(1000, 1000)
    wave += 1
    enemies_left = len(s.container)

# Main loop
while True:
  logic()
s.wn.mainloop()
