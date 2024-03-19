# Set the number of disks in the Tower of Hanoi puzzle
NUMBER_OF_DISKS = 4
# Calculate the total number of moves required to solve the puzzle
number_of_moves = 2 ** NUMBER_OF_DISKS - 1

# Initialize the rods with disks arranged on rod 'A' and empty 'B' and 'C'
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

# Function to perform an allowed move between two rods
def make_allowed_move(rod1, rod2):
    forward = False  # Initialize a flag to determine the direction of the move
    # Check if the move can be made forward (from rod1 to rod2)
    if not rods[rod2]:  # If rod2 is empty, the move is allowed
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:  # If the top disk on rod1 is smaller than the top disk on rod2, the move is allowed
        forward = True
    
    # Execute the move based on the direction determined
    if forward:
        # Moving disk from rod1 to rod2
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())  # Remove the top disk from rod1 and add it to rod2
    else:
        # Moving disk from rod2 to rod1 if the forward move is not allowed
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())  # Remove the top disk from rod2 and add it to rod1
    
    # Display the current state of the rods
    print(rods, '\n')

# Function to solve the Tower of Hanoi puzzle iteratively
def move(n, source, auxiliary, target):
    # Display starting configuration
    print(rods, '\n')
    # Iterate over the total number of moves
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        # Determine which move is allowed based on the current iteration and the parity of the number of disks
        if remainder == 1:
            # For every first of three moves, determine the move based on the parity of n
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            # For every second of three moves, alternate the allowed move based on the parity of n
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            # For every third move, the allowed move is always between the auxiliary and the target
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)

# Start solving the puzzle with the initial call
move(NUMBER_OF_DISKS, 'A', 'B', 'C')

# ------------------------------------------------------------------------------------------------------------- #

# solved using recursion instead of iterables
""" # Set the total number of disks in the Tower of Hanoi puzzle
NUMBER_OF_DISKS = 5
# Initialize the source rod 'A' with disks arranged from largest (at the bottom) to smallest (at the top)
A = list(range(NUMBER_OF_DISKS, 0, -1))
# Initialize the auxiliary and target rods 'B' and 'C' as empty
B = []
C = []

# Define the function to move disks
def move(n, source, auxiliary, target):
    # Base case: if there are no disks to move, just return
    if n <= 0:
        return
    
    # Recursive case 1: Move n - 1 disks from source to auxiliary,
    # using the target as a temporary placeholder
    move(n - 1, source, target, auxiliary)
    
    # Move the nth (bottom-most) disk from source to target
    # This is the "actual move" part of the recursion, where a disk is physically moved
    target.append(source.pop())
    
    # Display the current state of the rods
    # This helps visualize the progress of the algorithm
    print(A, B, C, '\n')
    
    # Recursive case 2: Move the n - 1 disks that were placed on the auxiliary
    # onto the target, using the source as a temporary placeholder now
    move(n - 1, auxiliary, source, target)
              
# Start the recursive process by moving all disks from rod A to rod C,
# with rod B serving as the auxiliary space
move(NUMBER_OF_DISKS, A, B, C) """
