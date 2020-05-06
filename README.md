# 8_puzzle_solver
A python code that solves 8-puzzle-problem by using BFS, DFS, UCS and A Star algorithms.

Given an initial state in a text file, the code tries to find the solution to its hardcoded goal state. Put the text file in the same directory with the ".py" file and change the function in the main according to the algorithms you want to use. It prints the required path for the black area (zero), the depth length, total number of nodes expanded and the initial and final states of the board.

i.e. Possible Output for A*:

['up', 'up', 'right', 'down', 'left', 'up', 'right', 'right', 'down', 'down']

The depth is 10

Total Expanded Nodes = 53 

Initial Board State:
-------------
| 5 | 4 | 2 |
-------------
| 7 | 1 | 3 |
-------------
| 0 | 8 | 6 |
-------------
Final Board State:
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 0 |
-------------

Process finished with exit code 0
