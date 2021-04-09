class MazeBase:
    def __init__(self, height, width):
        self._height = 2 * height + 1
        self._width = 2 * width + 1
        self._container = [[1 for _ in range(self._width)] for _ in range(self._height)]

        self.start = (1, 1)
        self.finish = (self._height - 2, self._width - 2)
        pass

    def get_cell(self, cell):
        if self.is_inside(cell):
            return self._container[cell[0]][cell[1]]

    def set_cell(self, cell, value):
        self._container[cell[0]][cell[1]] = value

    def can_move(self, cell):
        if cell[0] <= 0 or cell[0] >= self._height - 1:
            return False
        if cell[1] <= 0 or cell[1] >= self._width - 1:
            return False
        if self.get_cell(cell) == 0:
            return True
        else:
            return False

    def is_inside(self, cell):
        if cell[0] < 1 or cell[0] >= self._height - 1:
            return False
        if cell[1] < 1 or cell[1] >= self._width - 1:
            return False
        return True

    def print(self):
        for i in range(self._height):
            for j in range(self._width):
                if self._container[i][j] == 1:
                    print("\033[44m  \033[0m", end='')
                elif self._container[i][j] == 0:
                    print("\033[47m  \033[0m", end='')
            print()
        pass

    def export_to(self, file):
        for i in range(self._height):
            for j in range(self._width):
                file.write(self._container[i][j])
                file.write(" ")
            file.write("\n")

    def import_from(self, file):
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            if line[-1] == ' ':
                line = line[:-1]
            self._container.append(list(map(int, line.split(" "))))


