"""
bubble sort algorithm in python
"""
def bubble_sort(array,verbose=False):
    verboseprint = print if verbose else lambda *a, **k: None
    # find out array length
    n = len(array)
    # loop through array n times
    verboseprint('array to be sorted is {}'.format(array))
    for i in range(n):
        # initialize swapped variable
        verboseprint('{}th pass through array'.format(i+1))
        swapped = False
        # loop through first n-i elements
        # last i elements have been sorted already
        for j in range(0,n-i-1):
            # swap elements if necessary
            if array[j] > array[j+1]:
                verboseprint('swapping {} with {}'.format(array[j],array[j+1]))
                array[j], array[j+1] = array[j+1], array[j]
                # update swapped variable
                swapped = True
        # break loop if there has been no swapping in the last loop
        if swapped == False:
            break
        verboseprint('array after {}th pass is {}'.format(i+1,array))
    verboseprint('sorted array is {}'.format(array))
    return array

if __name__ == "__main__":
    array = [63, 34, 25, 12, 22, 11, 90]
    bubble_sort(array,verbose=True)

"""
output:
array to be sorted is [63, 34, 25, 12, 22, 11, 90]
1th pass through array
swapping 63 with 34
swapping 63 with 25
swapping 63 with 12
swapping 63 with 22
swapping 63 with 11
array after 1th pass is [34, 25, 12, 22, 11, 63, 90]
2th pass through array
swapping 34 with 25
swapping 34 with 12
swapping 34 with 22
swapping 34 with 11
array after 2th pass is [25, 12, 22, 11, 34, 63, 90]
3th pass through array
swapping 25 with 12
swapping 25 with 22
swapping 25 with 11
array after 3th pass is [12, 22, 11, 25, 34, 63, 90]
4th pass through array
swapping 22 with 11
array after 4th pass is [12, 11, 22, 25, 34, 63, 90]
5th pass through array
swapping 12 with 11
array after 5th pass is [11, 12, 22, 25, 34, 63, 90]
6th pass through array
sorted array is [11, 12, 22, 25, 34, 63, 90]
"""