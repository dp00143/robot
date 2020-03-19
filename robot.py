directions = ["N", "E", "S", "W"]
board = [5, 5]

class Robot():

    def __init__(self):
        self.x = -1
        self.y = -1
        self.f = None
        self.placed = False

    def place(self, x, y, f):
        if x < 0 or x > (board[0]-1) or y < 0 or y > (board[1]-1) or f not in directions:
            print "Invalid input for place x: %i, y: %i, f:%s" % (x, y, f)
            return
        self.placed = True
        self.x = x
        self.y = y
        self.f = f

    def move(self):
        if not self.placed:
            return
        if self.f is "N":
            self.y = self.y + 1 if self.y < (board[1]-1) else self.y
        if self.f is "S":
            self.y = self.y - 1 if self.y > 0 else self.y
        if self.f is "E":
            self.x = self.x + 1 if self.x < (board[0]-1) else self.x
        if self.f is "W":
            self.x = self.y - 1 if self.x > 0 else self.x

    def right(self):
        if not self.placed:
            return
        dir_index = directions.index(self.f)
        dir_index = (dir_index+1) % 4
        self.f = directions[dir_index]

    def left(self):
        if not self.placed:
            return
        dir_index = directions.index(self.f)
        dir_index = (dir_index-1) % 4
        self.f = directions[dir_index]

    def report(self):
        if not self.placed:
            return
        print "Current status is x: %i, y: %i, f:%s" % (self.x, self.y, self.f)


if __name__ == '__main__':
    r1, r2, r3 = Robot(), Robot(), Robot()
    print "###############"
    print "Robot 1"
    print "###############"
    r1.place(0, 0, "N")
    r1.move()
    r1.report()
    print "###############"
    print "Robot 2"
    print "###############"
    r2.place(0, 0, "N")
    r2.left()
    r2.report()
    print "###############"
    print "Robot 3"
    print "###############"
    r3.place(1, 2, "E")
    r3.move()
    r3.move()
    r3.left()
    r3.move()
    r3.report()