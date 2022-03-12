import copy
from random import randrange

N = 4

# must be a number between 1 & 80
difficulty = 30

number_of_configurations = 100
# top, right, bottom, left
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def create_matrix(old_mat, old_block_pos, new_block_pos):
    new_mat = copy.deepcopy(old_mat)
    temp = new_mat[new_block_pos[0]][new_block_pos[1]]
    # putting a 0 into the new block position
    new_mat[new_block_pos[0]][new_block_pos[1]] = 0
    # putting the temp value into the old block position
    new_mat[old_block_pos[0]][old_block_pos[1]] = temp
    return new_mat


def is_legal(block_pos):
    return 0 <= block_pos[0] < N and 0 <= block_pos[1] < N


def shuffle(initial_tiles):
    old_pos = [3, 3]
    old_mat = copy.deepcopy(initial_tiles)

    for i in range(difficulty):
        index = randrange(4)
        new_pos = [old_pos[0] + row[index], old_pos[1] + col[index]]
        if is_legal(new_pos):
            new_mat = create_matrix(old_mat, old_pos, new_pos)
            old_pos = new_pos
            old_mat = new_mat

    return old_mat


if __name__ == "__main__":
    f = open('permutatations.txt', 'w')
    initial_main = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    block_pos_main = [3, 3]
    for i in range(number_of_configurations):
        new_mat = shuffle(initial_main)
        print(new_mat, file=f)
