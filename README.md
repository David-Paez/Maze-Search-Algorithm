# Maze Search Algorithm

This is a Maze Search python script that I wrote for my Artificial Intelligence course. search.py is a script that has an agent traverse through a 
given Maze txt file where "%" are obstacles, "P" is the goal, and "." 
is the starting point. The agent can use four different algorithms to 
search through the Maze: Breadth, Depth, Greedy Best First, and A* Search. Any .txt file may be used as long as it is constructed with blank characters, % characters, and the characters "." to signal the initial state and "P" to signal the goal state. This folder already includes 5 sample mazes that can be used. 

## How to use

search.py can be ran on the terminal using Python 3. The script has an h flag to display the help message, and a method flag for the user to select which of the four algorithms to use: **breadth, depth, greedy, or astar**. By default, the method will be "breadth" if the user does not put in a valid method or does not put one in. The script does require the user to put in a string for the .txt file. If it is not a valid name (does not exist or spelled incorrectly), the program will terminate. 

Here is the usage: 
```bash
usage: search.py [-h] [--method METHOD] maze
```