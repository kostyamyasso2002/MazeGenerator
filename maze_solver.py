from maze_base import MazeBase
from maze_generaror import MazeGenerator


class MazeSolver(MazeGenerator):

    def __init__(self, height, width):
        super().__init__(height, width)
        self.path = set()

    def find_path(self):
        def get_neighbours(cell):
            for move in moves:
                new_cell = (cell[0] + move[0], cell[1] + move[1])
                if self.is_inside(new_cell) and self.get_cell(new_cell) == 0:
                    yield new_cell

        def dfs(cell):
            f = self.finish not in used
            used.add(cell)
            for neighbour in get_neighbours(cell):
                if neighbour not in used:
                    dfs(neighbour)
                if self.finish in used and f:
                    self.path.add(cell)
            pass

        used = set()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dfs(self.start)

    def print(self):
        for i in range(self._height):
            for j in range(self._width):
                if (i, j) in self.path:
                    print("\033[46m  \033[0m", end='')
                elif self._container[i][j] == 1:
                    print("\033[44m  \033[0m", end='')
                elif self._container[i][j] == 0:
                    print("\033[47m  \033[0m", end='')
            print()
