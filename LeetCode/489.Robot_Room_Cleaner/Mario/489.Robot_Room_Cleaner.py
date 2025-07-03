#!/usr/bin/env python3

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # room = m * n  0: wall / 1: slot
        # turnLeft: up -> left - > down -> right
        # turnRight: up -> right -> down -> left

        vis = set()  # (row, col)
        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        # r: row, c: column, d:direction
        def backtrack(r, c, d):

            vis.add((r, c))
            robot.clean()

            for i in range(4):
                nd = (d + i) % 4

                nr, nc = r + DIRS[nd][0], c + DIRS[nd][1]
                if (nr, nc) not in vis and robot.move():
                    backtrack(nr, nc, nd)
                    go_back()

                robot.turnRight()

        backtrack(0, 0, 0)
