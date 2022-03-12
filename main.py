import ast
import copy
import time
import matplotlib.pyplot as plt
import statistics

from DataStructure import DataStructure
from QueueNode import Node

N = 4
SOLUTION = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

# top, right, bottom, left
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def calculate_cost(matrix):
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] and matrix[i][j] != SOLUTION[i][j]:
                count += 1
    return count


def calculate_block_pos(mat):
    for i in range(N):
        for y in range(N):
            if mat[i][y] == 0:
                return [i, y]


def is_legal(block_pos):
    return 0 <= block_pos[0] < N and 0 <= block_pos[1] < N


def create_matrix(old_mat, old_block_pos, new_block_pos):
    new_mat = copy.deepcopy(old_mat)
    temp = new_mat[new_block_pos[0]][new_block_pos[1]]
    # putting a 0 into the new block position
    new_mat[new_block_pos[0]][new_block_pos[1]] = 0
    # putting the temp value into the old block position
    new_mat[old_block_pos[0]][old_block_pos[1]] = temp
    return new_mat


def print_matrix(mat):
    print('\n'.join(['\t'.join([str(cell) for cell in j]) for j in mat]))


def print_path(root):
    if root is None:
        return

    print_path(root.parent)
    print("Level is: ", root.level)
    print_matrix(root.matrix)
    print()


def branch_and_bound(initial_matrix, initial_block_pos):
    boards_seen = []
    start = time.time()
    # priority queue to store the live nodes
    liveNodes = DataStructure()
    boards_seen.append(initial_matrix)

    # create root node
    root_cost = calculate_cost(initial_matrix)
    root = Node(None, initial_matrix, root_cost, initial_block_pos, 0)
    liveNodes.push(root)

    while not liveNodes.empty():
        min_node = liveNodes.pop()
        print_matrix(min_node.matrix)
        print("COST IS: " + str(min_node.cost) + ", LEVEL IS: " + str(min_node.level))

        # if this node is the answer
        if min_node.cost == 0:
            stop = time.time()
            print("\n\n***** SOLUTION FOUND *****\n")
            # print_path(min_node)
            return min_node.level, stop - start, len(boards_seen)

        # create the new children
        for i in range(4):
            child_block_pos = [min_node.block_pos[0] + row[i], min_node.block_pos[1] + col[i]]
            if is_legal(child_block_pos):
                child_matrix = create_matrix(min_node.matrix, min_node.block_pos, child_block_pos)
                if child_matrix not in boards_seen:
                    boards_seen.append(child_matrix)
                    child_cost = calculate_cost(child_matrix)
                    child = Node(min_node, child_matrix, child_cost, child_block_pos, min_node.level + 1)
                    liveNodes.push(child)


def draw_graph(numbers, ylabel):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    mean = statistics.mean(numbers)
    ax.axhline(mean, color="gray")
    ax.text(1.02, mean, str(mean), va='center', ha="left", bbox=dict(facecolor="w", alpha=0.5),
            transform=ax.get_yaxis_transform())
    plt.axhline(y=mean, color='r', linestyle='-')
    plt.plot(numbers, color='b')
    plt.ylabel(ylabel)
    plt.xlabel('Tiles Configurations')
    plt.show()


if __name__ == "__main__":
    levels, running_times, tree_sizes = [], [], []
    file = open('permutatations.txt', 'r')
    for line in file:
        initial_main = ast.literal_eval(line)
        block_pos_main = calculate_block_pos(initial_main)
        l, r, t = branch_and_bound(initial_main, block_pos_main)
        levels.append(l)
        running_times.append(r)
        tree_sizes.append(t)

    draw_graph(levels, 'Tree Depth')
    draw_graph(running_times, 'Running Time')
    draw_graph(tree_sizes, 'N. Of States')
