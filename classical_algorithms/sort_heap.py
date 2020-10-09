"""
heap sort
"""
from heapq import heappush, heappop

def heap_sort(array):
    # initialize temp array
    temp_array = []
    # push to temp array as a heap
    [heappush(temp_array,value) for value in array]
    # pop from temp array and return resulting array
    return [heappop(temp_array) for _ in array]

if __name__ == "__main__":
    array = [2,4,1,4,7,34,4,5,7,1]
    sorted_array = heap_sort(array)
    print(sorted_array)