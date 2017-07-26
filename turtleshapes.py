import turtle

num_pts=10

for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(100)
    turtle.right(180/num_pts)

turtle.mainloop()
