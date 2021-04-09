from maze import Maze
from maze_walker import MazeWalker
from maze_solver import MazeSolver
import maze_walker
import keyboard
from enum import Enum
import time
import os

rr = time.time()
a = MazeSolver(20, 20)
a.generate_prim()

a.find_path()
a.print()
print(time.time() - rr)
