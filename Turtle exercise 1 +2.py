from  turtle import *
def draw_square(lengt,colour) :
    for i in range(4) :

        color(colour)
        forward(lengt)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
# Sửa biến color thanh tên khác là được

