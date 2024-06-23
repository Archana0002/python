def print_pyramid(n):
    max_width = 2 * n - 1
    
    for i in range(1, n + 1):
        num_stars = 2 * i - 1
        num_spaces = max_width - num_stars
        
        # Construct the line with spaces and stars
        line = ' ' * num_spaces + '* ' * num_stars
        # Remove the trailing space at the end of the line
        line = line.rstrip()
        
        print(line)

# Reading input
import sys
input = sys.stdin.read().strip().split()

# Ensure there's at least one item in input to prevent IndexError
if len(input) > 0:
    T = int(input[0])
    testcases = list(map(int, input[1:1+T]))

    for n in testcases:
        print_pyramid(n)
        if n > 0:
            print()  # Blank line between consecutive test cases
