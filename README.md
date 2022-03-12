# 15-Puzzle Optimization Using Branch & Bound

You can find all information about this project at: [report](https://github.com/saraspagno/15-Puzzle_BranchAndBound/blob/main/Report.pdf)

This code will take as input a list of initial tiles configurations,and solve them using the Branch & Bound method, either with BFS or DFS. 
For each solution it will save: 
* The number of moves in the optimal solution found
* The running time it took to find the solution
* The number of nodes in tree at the time of finding the solution

It will then take these 3 parameters and output 3 graphs showing the average among all of the input confgurations.

### Instructions for running this project
1. Create a `permutations.txt` file containing the initial tiles' configurations using `PermutationsMaker.py`
   * In `PermutationsMaker`, change the gloabal var `difficulty` to determine the difficulty of the scrable
   * In `PermutationsMaker`, change the gloabal var `number_of_configurations` to determine the number of initial configurations in the input file
   * Run the `PermutationsMaker.py`file
2. Decide whether to use a BFS or DFS method (Stack or Queue)
   * In the `main.py` file you can write `from QueueNode import Node` to use a DFS method - or
   * In the `main.py` file you can write `from StackNode import Node` to use a BFS method
3. Run the `main.py`file

At the end of the running, you will be able to see the 3 graphs mentioned above based on your intial choices.   

For each starting configuration, to see the found moves' sequence from the it to the goal configuration, uncomment the `print_path(min_node)` in line 83.
 
