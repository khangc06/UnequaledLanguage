import Turtle1

class Artist:

    def __init__(self, t):
        self.t = t

    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def square(self, size = 200):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)
    #def star(self, size = 100):
        
    def circle(self, size = 1):
        for i in range(360):
            self.t.right(1)
            self.t.forward(1)

    def star(self, size =1):
        for i in range(5):
            self.t.forward(100)
            self.t.right(144)
            self.t.forward(size)
    def hexagon(self, size = 100):
        for i in range(6):
            self.t.forward(size)
            self.t.right(60)

    def trapezoid(self, size = 100, sizetop=120, sizebottom = 180):
        for i in range(1):
            self.t.right(18)
            self.t.forward(size)
            self.t.right(72)
            self.t.forward(sizetop)
            self.t.right(72)
            self.t.forward(size)
            self.t.right(108)
            self.t.forward(sizebottom)

    def parallelogram(self, size = 180):
        for i in range(2):
            self.t.forward(size)
            self.t.right(78)
            self.t.forward(size)
            self.t.right(102)
            
            
            
        

    def move (self, x, y):
        self.t.penup()
        self.t.gota(x, y)
        self.t.pendown()


def main():
    canvas = Turtle1.Screen()
    canvas.bgcolor("cyan")
    canvas.title("Turtle example")

    t=Turtle1.Turtle()
    t.shape("turtle")
    t.speed(1)
    t.forward(100)
    t.penup()
    t.forward(100)
    t.pendown()
    t.forward(100)


    art=Artist(t)
    art.triangle()
    art.square()

    art.circle()
    art.star()


    art.hexagon()

    art.trapezoid()

    art.parallelogram()
 
    

if __name__ =="__main__":
    main()
