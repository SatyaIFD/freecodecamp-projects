# Number of disks to move
NUMBER_OF_DISKS = 5

# Rods: A = source, B = auxiliary, C = target
A = list(range(NUMBER_OF_DISKS, 0, -1))  # e.g., [5, 4, 3, 2, 1]
B = []
C = []

def move(n, source, auxiliary, target):
    # Base case: No disk to move
    if n <= 0:
        return

    # Step 1: Move (n-1) disks from source to auxiliary
    move(n - 1, source, target, auxiliary)

    # Step 2: Move the nth (largest) disk from source to target
    target.append(source.pop())

    # Step 3: Display the current state of all rods
    print(A, B, C, '\n')

    # Step 4: Move (n-1) disks from auxiliary to target
    move(n - 1, auxiliary, source, target)

# Start the recursive Tower of Hanoi solution
move(NUMBER_OF_DISKS, A, B, C)
