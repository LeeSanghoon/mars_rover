
class MarsRover(object):

    rotate_left = {
        'N' : 'W',
        'E' : 'N',
        'W' : 'S',
        'S' : 'E'
    }

    rotate_right = {
        'N' : 'E',
        'E' : 'S',
        'W' : 'N',
        'S' : 'W'
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction    # N, E, W, S

    def move(self):
        if self.direction == 'N':
            self.y = self.y + 1
        elif self.direction == 'E':
            self.x = self.x + 1
        elif self.direction == 'W':
            self.x = self.x - 1
        elif self.direction == 'S':
            self.y = self.y - 1

    def rotate(self,orientation):
        if orientation == 'L':
            self.direction = self.rotate_left[self.direction]
        else: # R
            self.direction = self.rotate_right[self.direction]

    def __str__(self):
        return '%d %d %c' % (self.x, self.y, self.direction)

class Plateau(object):
    def __init__(self, plateau_size):
        self.plateau_size = plateau_size

    def set_mars_rover(self, mars_rover):
        self.mars_rover = mars_rover

    def move_mars_rover(self, moves):
        for move in moves:
            if move == 'L' or move == 'R':
                self.mars_rover.rotate(move)
            else: # M
                self.mars_rover.move()

if __name__=="__main__":
    import sys, os

    if len(sys.argv) != 2:
        print 'usage: python MarsRover.py input_file'
        exit(-1)

    input_file = sys.argv[1]

    f = open(input_file)

    line = f.readline()
    plateau_size = map(int, line.split())

    plateau = Plateau(plateau_size)

    while True:
        line1 = f.readline()
        line2 = f.readline()
        if not line1 or not line2:
            break
        (x, y, d) = line1.split()
        moves = line2.strip()

        mars_rover = MarsRover(int(x), int(y), d)
        plateau.set_mars_rover(mars_rover)
        plateau.move_mars_rover(moves)

        print mars_rover

    f.close()

