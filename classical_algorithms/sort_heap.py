"""
heap sort
"""
from heapq import heappush, heappop

def heap_sort(array,verbose=False):
    verboseprint = print if verbose else lambda *a, **k: None
    verboseprint('array to be sorted is {}'.format(array))
    # initialize temp array
    temp_array = []
    # push to temp array as a heap
    [heappush(temp_array,value) for value in array]
    verboseprint('heap is {}'.format(temp_array))
    # pop from temp array and return resulting array
    sorted_array = [heappop(temp_array) for _ in array]
    verboseprint('sorted array is {}'.format(sorted_array))
    return sorted_array

if __name__ == "__main__":
    array = [2,4,1,4,7,34,4,5,7,1]
    sorted_array = heap_sort(array,verbose=True)

"""
output:
array to be sorted is [2, 4, 1, 4, 7, 34, 4, 5, 7, 1]
heap is [1, 1, 2, 4, 4, 34, 4, 5, 7, 7]
sorted array is [1, 1, 2, 4, 4, 4, 5, 7, 7, 34]
"""