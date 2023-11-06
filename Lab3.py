import turtle

t = turtle.Pen()

def rechteck():
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)



    t.penup()
    t.right(90)
    t.forward(40)
    t.pendown()
    t.left(90)


    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)

t.reset()

def curv():
    for i in range(200):
        t.right(1)
        t.forward(1)

def herz():
    t.left(140)
    t.forward(113)
    curv()
    t.left(120)
    curv()
    t.forward(113)


t.reset()

def haus():
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    for i in range(3):
        t.forward(150)
        t.left(120)

    t.right(90)

    for i in range(4):
        t.forward(150)
        t.left(90)

    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.left(90)

    for i in range(3):
        t.forward(150)
        t.left(120)

    t.right(90)

    for i in range(4):
        t.forward(150)
        t.left(90)

    t.penup()
    t.goto(-125, -50)
    t.pendown()

    for i in range(2):
        t.forward(-70)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.penup()
    t.goto(175, -50)
    t.pendown()

    for i in range(2):
        t.forward(-70)
        t.left(90)
        t.forward(30)
        t.left(90)

    t.penup()
    t.goto(-190, 70)
    t.pendown()

    for _ in range(4):
        t.forward(30)
        t.left(90)

    t.penup()
    t.goto(110, 70)
    t.pendown()

    for _ in range(4):
        t.forward(30)
        t.left(90)


t.reset()

def main():
    print("Bitte wählen Sie eine Zeichnung aus dem Menü aus: ")
    print('''
    1. Rechteck
    2. Herz
    3. Haus  ''')
    choice = input("Geben Sie die gewünschte Nummer ein: ")

    if choice == "1":
        rechteck()
    elif choice == "2":
        herz()
    elif choice == "3":
        haus()

main()