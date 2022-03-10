# queue
class Node:
    def __init__(self, parent, matrix, cost, block_pos, level):
        # the parent node board
        self.parent = parent
        # the number matrix configuration of this node
        self.matrix = matrix
        # c(x) of the node
        self.cost = cost
        # the position of the empty block in the board
        self.block_pos = block_pos
        # the level of the node in the tree
        self.level = level

    # method for priority queue
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.level < other.level
        return self.cost < other.cost
