from collections import deque

# Define generator function to search pattern in file
def search(lines, pattern, history=5):
    # define deque and set maxlen parameter in previous lines
    previous_lines = deque(maxlen=history)
    # iterate through lines
    for line in lines:
        # yield line and previous lines if pattern is present
        if pattern in line:
            yield line, previous_lines
        # append line to previous lines
        previous_lines.append(line)

# Use generator function to print the line and previous 3 lines
if __name__ == '__main__':
    # open text file to perform search
    with open('test_cases/alice_in_wonderland.txt') as f:
        # get line and previous lines where pattern is found
        for line, prevlines in search(f, 'Lewis', 3):
            # print previous lines
            for pline in prevlines:
                print(pline, end='')
            # print line
            print(line, end='')
            # print separator
            print('-'*20)