import turtle

# Fungsi untuk menggambar persegi panjang
def draw_rectangle():
    for _ in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

# Fungsi untuk menggambar segitiga
def draw_triangle():
    for _ in range(3):
        turtle.forward(150)
        turtle.left(120)

# Fungsi untuk menggambar trapezium
def draw_trapezium():
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(200)
    turtle.left(45)
    turtle.forward(100)

# Fungsi untuk menggambar jajar genjang
def draw_parallelogram():
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)

# Fungsi untuk menggambar belah ketupat
def draw_rhombus():
    for _ in range(2):
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(100)
        turtle.left(120)

# Inisialisasi modul Turtle
turtle.speed(1)  # Kecepatan gambar (1 adalah lambat)

# Gambar bangun datar
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
draw_rectangle()
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
draw_triangle()
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
draw_trapezium()
turtle.penup()
turtle.goto(200, 100)
turtle.pendown()
draw_parallelogram()
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
draw_rhombus()

# Tutup jendela Turtle saat selesai
turtle.done()