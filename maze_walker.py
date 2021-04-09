import os
import time

import keyboard

from maze_generaror import MazeGenerator
from enum import Enum

class Direction(Enum):
    NONE = (0, 0)
    DOWN = (1, 0)
    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class MazeWalker(MazeGenerator):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.position = self.start

    def move(self, direction):
        new_position = (self.position[0] + direction.value[0], self.position[1] + direction.value[1])
        if self.can_move(new_position):
            self.position = new_position
        pass

    def print(self):
        for i in range(self._height):
            for j in range(self._width):
                if (i, j) == self.position:
                    print("\033[46m  \033[0m", end='')
                elif (i, j) == self.start:
                    print("\033[42m  \033[0m", end='')
                elif (i, j) == self.finish:
                    print("\033[41m  \033[0m", end='')
                elif self._container[i][j] == 1:
                    print("\033[44m  \033[0m", end='')
                elif self._container[i][j] == 0:
                    print("\033[47m  \033[0m", end='')
            print()

    def successful(self):
        return self.position == self.finish


def game(maze):
    direct = Direction.NONE
    while True:
        if direct != Direction.NONE:
            time.sleep(0.1)
        direct = Direction.NONE
        for _ in range(100):
            time.sleep(0.001)
            if keyboard.is_pressed('a'):
                direct = Direction.LEFT
            elif keyboard.is_pressed('w'):
                direct = Direction.UP
            elif keyboard.is_pressed('s'):
                direct = Direction.DOWN
            elif keyboard.is_pressed('d'):
                direct = Direction.RIGHT

        maze.move(direct)
        os.system("clear")
        maze.print()
        if maze.successful():
            print("УРА!")
            return
