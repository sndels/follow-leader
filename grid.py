class Grid():
    def __init__(self):
        self.cells = []
        for i in range(35):
            self.cells.append([])
            for j in range(27):
                self.cells[i].append([])

    def remove(self, follower, x, y):
        if x > 0 and x < len(self.cells) and y > 0 and y < len(self.cells[0]):
            self.cells[x][y].remove(follower)

    def insert(self, follower, x, y):
        if x > 0 and x < len(self.cells) and y > 0 and y < len(self.cells[0]):
            self.cells[x][y].append(follower)

    def getNeighbours(self, x, y):
        neighbours = []
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                if i > 0 and i < len(self.cells) and j > 0 and j < len(self.cells[0]):
                    neighbours += self.cells[i][j]
        return neighbours
