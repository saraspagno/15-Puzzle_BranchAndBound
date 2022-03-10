import copy
from DataStructure import DataStructure
from StackNode import Node
# from QueueNode import Node

N = 4
SOLUTION = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

boards_seen = []

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
            print("\n\n***** DONE, PRINTING PATH *****\n")
            print_path(min_node)
            return

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


if __name__ == "__main__":
    initial_main = [[2, 6, 4, 12], [1, 7, 9, 8], [15, 13, 14, 3], [5, 10, 11, 0]]
    block_pos_main = [3, 3]
    branch_and_bound(initial_main, block_pos_main)

