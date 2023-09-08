import turtle

# Fungsi menggambar sesuatu sesuai kreasi Anda
def draw_custom_shape():
    # Anda dapat mengganti ini dengan apa pun yang Anda inginkan
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

# Inisialisasi turtle
turtle.speed(1)

# Panggil fungsi untuk menggambar sesuatu sesuai kreasi Anda
draw_custom_shape()

# Tutup jendela saat selesai
turtle.exitonclick()