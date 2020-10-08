#!/bin/python3

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # initialize operations_array with 1 extra value 
    operations_array = [0]*(n+1)
    # loop through queries to update operations array
    for query in queries:
        # all values after first index will be added by value
        operations_array[query[0]-1] += query[2]
        # all values after second index will be subtracted by value
        operations_array[query[1]] -= query[2]
    # initialize temp and max values
    temp_value = 0
    max_value = -99999999
    # loop through array
    for value in operations_array:
        # add array value to temp_value to get value that would have been
        temp_value += value
        # update max value if necessary
        if temp_value > max_value:
            max_value = temp_value
    return max_value

if __name__ == '__main__':

    n = int(5)

    queries = [[1,2,100],[2,5,100],[3,4,100]]

    result = arrayManipulation(n, queries)

    print(result)