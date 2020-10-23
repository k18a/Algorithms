""""
radix sort
"""
from sort_counting import counting_sort

def radix_sort(array, verbose = False):
    # get array maximum
    maximum = max(array)
    # initialize exponent
    exponent = 1

    # check if exponent is greater than max
    while exponent < maximum:
        # count sort array for the given exponent
        counting_sort(array,inplace=True,exponent=exponent,verbose=verbose)
        # multiply exponent by 10
        exponent *= 10
    
    return array

if __name__ == "__main__":
    array = [170,45,90,802,24,2,66]
    radix_sort(array, verbose=True)

"""
output:
array to be sorted is [170, 45, 90, 802, 24, 2, 66]
count array for exponent 1 is [2, 2, 4, 4, 5, 6, 7, 7, 7, 7]
index 6 in input array goes to index 6 in output array
index 5 in input array goes to index 3 in output array
index 4 in input array goes to index 4 in output array
index 3 in input array goes to index 2 in output array
index 2 in input array goes to index 1 in output array
index 1 in input array goes to index 5 in output array
index 0 in input array goes to index 0 in output array
sorted array is [170, 90, 802, 2, 24, 45, 66]
array to be sorted is [170, 90, 802, 2, 24, 45, 66]
count array for exponent 10 is [2, 2, 3, 3, 4, 4, 5, 6, 6, 7]
index 6 in input array goes to index 4 in output array
index 5 in input array goes to index 3 in output array
index 4 in input array goes to index 2 in output array
index 3 in input array goes to index 1 in output array
index 2 in input array goes to index 0 in output array
index 1 in input array goes to index 6 in output array
index 0 in input array goes to index 5 in output array
sorted array is [802, 2, 24, 45, 66, 170, 90]
array to be sorted is [802, 2, 24, 45, 66, 170, 90]
count array for exponent 100 is [5, 6, 6, 6, 6, 6, 6, 6, 7, 7]
index 6 in input array goes to index 4 in output array
index 5 in input array goes to index 5 in output array
index 4 in input array goes to index 3 in output array
index 3 in input array goes to index 2 in output array
index 2 in input array goes to index 1 in output array
index 1 in input array goes to index 0 in output array
index 0 in input array goes to index 6 in output array
sorted array is [2, 24, 45, 66, 90, 170, 802]
"""