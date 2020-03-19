from robot import Robot

if __name__ == '__main__':
    f = open("commands.txt")
    robot = Robot()

    for line in f:
        args = line.strip().split(" ")
        if line.startswith("PLACE"):
            robot.place(int(args[1]), int(args[2]), args[3])
        if line.startswith("MOVE"):
            robot.move()
        if line.startswith("LEFT"):
            robot.left()
        if line.startswith("RIGHT"):
            robot.right()
        if line.startswith("REPORT"):
            robot.report()
