import random
import time
import os
from maze_solver import MazeSolver
from maze_generaror import MazeGenerator

random.seed(time.time())


class Maze(MazeSolver, MazeGenerator):
    def __init__(self, height, width):
        super().__init__(height, width)
