alien = Actor('truck')
alien.pos = 100, 10
alien.angle += 90

WIDTH = 1000
HEIGHT = 500

def update():
    alien.angle += 1

def draw():
    screen.clear()
    alien.draw()
