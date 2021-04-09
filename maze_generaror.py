from maze_base import MazeBase
import random
import sys
import time
import os
from collections import Counter

sys.setrecursionlimit(10000)


class MazeGenerator(MazeBase):

    def __init__(self, height, width):
        super().__init__(height, width)

    def generate_dfs(self):
        def get_neighbours(cell):
            ans = []
            for move in moves:
                new_cell = (cell[0] + move[0], cell[1] + move[1])
                if self.is_inside(new_cell) and self.get_cell(new_cell) == 1:
                    ans.append(new_cell)
            return ans

        def dfs(cell):
            neighbours = get_neighbours(cell)
            while len(neighbours) > 0:
                cell_to = neighbours[random.randint(0, len(neighbours) - 1)]
                self.set_cell(cell_to, 0)
                self.set_cell(((cell[0] + cell_to[0]) // 2, (cell[1] + cell_to[1]) // 2), 0)

                #time.sleep(0.1)
                #os.system("clear")
                #self.print()
                #print()

                dfs(cell_to)
                neighbours = get_neighbours(cell)
            pass

        moves = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        self.set_cell(self.start, 0)
        dfs(self.start)
        pass

    def generate_prim(self):
        def get_walls(cell):
            for move in walls_direction:
                neib_wall = (cell[0] + move[0], cell[1] + move[1])
                if self.is_inside(neib_wall) and self.get_cell(neib_wall) == 1:
                    yield neib_wall

        def get_cells_from_wall(wall):
            if wall[0] % 2 == 0:
                return [(wall[0] - 1, wall[1]), (wall[0] + 1, wall[1])]
            else:
                return (wall[0], wall[1] - 1), (wall[0], wall[1] + 1)

        walls_direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.set_cell(self.start, 0)
        cells = set()
        cells.add(self.start)
        all_walls = set()
        cur_walls = set()
        for start_wall in get_walls(self.start):
            all_walls.add(start_wall)
            cur_walls.add(start_wall)

        while len(cur_walls) > 0:
            new_wall = random.choice(list(cur_walls))
            cell_1, cell_2 = get_cells_from_wall(new_wall)
            cur_walls.remove(new_wall)
            if self.can_move(cell_1) and self.can_move(cell_2):
                continue
            #time.sleep(0.1)
            #os.system("clear")
            #self.print()
            #print()
            if self.can_move(cell_1):
                temp = cell_1
                cell_1 = cell_2
                cell_2 = temp
                del temp
            self.set_cell(new_wall, 0)
            self.set_cell(cell_1, 0)
            for wall in get_walls(cell_1):
                if wall not in all_walls:
                    all_walls.add(wall)
                    cur_walls.add(wall)
