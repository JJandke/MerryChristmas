from turtle import *  # Bibliothek für grafische Oberfläche
from random import randint  # Zufallszahl für die Sterne


def hintergrund_erstellen(turtle, color, x, y, width, height):
    turtle.penup()  # Stift hochheben, damit er nicht zeichnet wenn er bewegt wird
    turtle.color(color)  # Stiftfarbe setzen
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()  # Stift auf's Papier setzen
    turtle.begin_fill()
    # Baumstamm zeichnen
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    # Baumstamm füllen
    turtle.end_fill()
    # Dreieck wieder in ursprungsstellung bringen
    turtle.setheading(0)


def kreis_erstellen(turtle, x, y, radius, color):
    ani.penup()
    ani.color(color)
    ani.fillcolor(color)
    ani.goto(x, y)
    ani.pendown()
    ani.begin_fill()
    ani.circle(radius)
    ani.end_fill()


###########################
# Anfangsparameter setzen #
###########################
BG_COLOR = "#00BFFF"  # Hintergrundfarbe setzen
ani = Turtle()
ani.speed(2)  # Zeichengeschwindigkeit setzen
screen = ani.getscreen()
screen.bgcolor(BG_COLOR)  # Hintergrundfarbe zuweisen
screen.title("Frohe Weihnachten!")  # Fenstertitel festlegen
screen.setup(width=1.0, height=1.0)  # Fenster auf maximale Bildschirmgröße anpassen
y = -100
hintergrund_erstellen(ani, "saddle brown", -15, y - 60, 30, 60)  # Zeichnen starten

#################
# Baum zeichnen #
#################
width = 240
ani.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width / 2
    hintergrund_erstellen(ani, "green", x, y, width, height)
    y = y + height

########################################
# Stern auf Christbaumspitze erstellen #
########################################
ani.speed(1)
ani.penup()
ani.color('yellow')
ani.goto(-20, y + 10)  # Koordinaten der Spitze
ani.begin_fill()
ani.pendown()
for i in range(5):
    ani.forward(40)
    ani.right(144)
ani.end_fill()

#################
# Mond zeichnen #
#################
tree_height = y + 40
kreis_erstellen(ani, 230, 180, 60, "yellow")     # ganzen Kreis zeichnen
kreis_erstellen(ani, 220, 180, 60, BG_COLOR)    # kleineren Kreis mit Hintergrundfarbe auf großen Kreis zeichnen, um eine Sichel zu erstellen


###################
# Sterne zeichnen #
###################
ani.speed(10)                       # bissl flotter machen
number_of_stars = randint(30, 40)   # Anzahl der Sterne ist zufällig aber auf [30;40] begrenzt
for _ in range(0, number_of_stars):
    x_star = randint(-(screen.window_width() // 2), screen.window_width() // 2)
    y_star = randint(tree_height, screen.window_height() // 2)
    size = randint(5, 20)
    ani.penup()
    ani.color('white')
    ani.goto(x_star, y_star)
    ani.begin_fill()
    ani.pendown()
    for i in range(5):
        ani.forward(size)
        ani.right(144)
    ani.end_fill()


###################
# Weihnachtsgrüße #
###################
ani.speed(1)
ani.penup()
msg = "Liebe Ani, ich wünsche dir und deiner ganzen Familie frohe Weihnachten!"
ani.goto(0, -200)
ani.color("white")
ani.pendown()
ani.write(msg, move=False, align="center", font=("Arial", 15, "bold"))

ani.hideturtle()
screen.mainloop()
