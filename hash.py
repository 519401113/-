import numpy

def create_hashboard(hashtable, board, width, height):
    a = 0
    for i in range(width):
        for j in range(height):
            b = board[i][j]
            if b != 0:
                a = a ^ hashtable.table()[board[b-1]][i][j]
    return a

class hash():
    def __init__(self, Width, Height):
        self.Zobrist1 = list(numpy.random.randint(low = 0, high = 9223372036854775807, size = (Width, Height), dtype= numpy.int64))
        self.Zobrist2 = list(numpy.random.randint(low = 0, high = 9223372036854775807, size = (Width, Height), dtype= numpy.int64))


    def table(self):
        return [self.Zobrist1, self.Zobrist2]


if __name__ == '__main__':
    print(hash(2,2).table()[0][1][1])