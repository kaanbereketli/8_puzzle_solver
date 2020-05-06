### Data Structures
# The goal is defined as:
#
# -------------
# | 1 | 2 | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 0 |
# -------------
#
# Where 0 denotes space.
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
total_expanded_nodes = 0
#
# The code will read state from a file called "state.txt" where the format is
# as above but space separated. i.e. the content for the goal state would be
# 1 2 3 4 5 6 7 8 0

#Code starts

from pythonds.basic.stack import Stack

def display_board(state):
    print("-------------")
    print("| %i | %i | %i |" % (state[0], state[1], state[2]))
    print("-------------")
    print("| %i | %i | %i |" % (state[3], state[4], state[5]))
    print("-------------")
    print("| %i | %i | %i |" % (state[6], state[7], state[8]))
    print("-------------")


def move_up(state):
    """Moves the zero up on the board. Returns a new state as a list."""
    # Make a copy of the list and find the index with the "0" value
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [0, 1, 2]:
        # Swap the values.
        new_state[index] , new_state[index - 3] = new_state[index - 3] , new_state[index]
        return new_state
    else:
        # Can't move, return None (Pythons NULL)
        return None


def move_down(state):
    """Moves the zero down on the board. Returns a new state as a list."""
    # Make a copy of the list and find the index with the "0" value
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [6, 7, 8]:
        # Swap the values.
        new_state[index] , new_state[index + 3] = new_state[index + 3] , new_state[index]
        return new_state
    else:
        # Can't move, return None.
        return None


def move_left(state):
    """Moves the zero left on the board. Returns a new state as a list."""
    # Make a copy of the list and find the index with the "0" value
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [0, 3, 6]:
        # Swap the values.
        new_state[index] , new_state[index - 1] = new_state[index - 1] , new_state[index]
        return new_state
    else:
        # Can't move it, return None
        return None


def move_right(state):
    """Moves the zero right on the board. Returns a new state as a list."""
    # Make a copy of the list and find the index with the "0" value
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [2, 5, 8]:
        # Swap the values.
        new_state[index] , new_state[index + 1] = new_state[index + 1] , new_state[index]
        return new_state
    else:
        # Can't move, return None
        return None


def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)


def expand_node(node):
    """Returns a list of expanded nodes"""
    global total_expanded_nodes
    expanded_nodes = []
    expanded_nodes.append(create_node(move_up(node.state), node, "u", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_down(node.state), node, "d", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_left(node.state), node, "l", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_right(node.state), node, "r", node.depth + 1, 0))
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # list comprehension!
    total_expanded_nodes = total_expanded_nodes + 1
    return expanded_nodes


def bfs(start, goal):
    """Performs a breadth first search from the start state to the goal"""
    # A list (can act as a queue) for the nodes.
    goal = goal
    start_node = create_node(start, None, None, 0, 0)
    fringe = []
    fringe.append(start_node)
    current = fringe.pop(0)
    path = []
    while (current.state != goal):
        fringe.extend(expand_node(current))
        current = fringe.pop(0)
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path
    pass


def dfs(start, goal, depth=10):
    start_node = create_node(start, None, None, 0, 0)
    fringe_stack = Stack()
    fringe_stack.push(start_node)
    current = fringe_stack.pop()
    path = []
    while (current.state != goal):
        temp = expand_node(current)
        for item in temp:
            fringe_stack.push(item)
        current = fringe_stack.pop()
        if (current.depth > 10):
            return None
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path


def uniform_cost(start, goal):
    start_node = create_node(start, None, None, 0, 0)
    fringe = []
    path = []
    fringe.append(start_node)
    current = fringe.pop(0)
    while (current.state != goal):
        temp = expand_node(current)
        for item in temp:
            item.depth += current.depth
            fringe.append(item)
        fringe.sort(key=lambda x: x.depth)
        current = fringe.pop(0)
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path


def a_star(start, goal):
    global total_expanded_nodes
    start_node = create_node(start, None, None, 0, 0)
    fringe = []
    path = []
    fringe.append(start_node)
    current = fringe.pop(0)
    while (current.state != goal):
        fringe.extend(expand_node(current))
        for item in fringe:
            h(item, goal)
            item.heuristic += item.depth
        fringe.sort(key=lambda x: x.heuristic)
        current = fringe.pop(0)
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path


def h(state, goal):
    global total_expanded_nodes
    dmatch = 0
    for i in range(0, 9):
        if state.state[i] != goal[i]:
            dmatch += 1
    state.heuristic = dmatch



# Node data structure
class Node:
    def __init__(self, state, parent, operator, depth, cost):
        global total_expanded_nodes
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost

        self.heuristic = None



def readfile(filename):
    f = open(filename)
    data = f.read()
    # Get rid of the newlines
    data = data.strip("n")
    # Break the string into a list using a space as a seperator.
    data = data.split(" ")
    state = []
    for element in data:
        state.append(int(element))
    return state


# Main method
def main():
    global total_expanded_nodes
    starting_state = readfile("state.txt")
    # Change this function to use bfs, dfs, uniform_cost or a_star
    result = a_star(starting_state, goal_state)
    if result == None:
        print("No solution found")
    elif result == []:
        print("Start node was the goal!")
    else:
        print(result)
        print("The depth is", len(result))
        print("Total Expanded Nodes =", total_expanded_nodes)


# A python-isim. Basically if the file is being run execute the main() function.
if __name__ == "__main__":
    main()