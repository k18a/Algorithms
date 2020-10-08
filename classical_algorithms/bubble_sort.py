"""
bubble sort algorithm in python
"""
def bubble_sort(array):
    # find out array length
    n = len(array)
    # loop through array n times
    for i in range(n):
        # initialize swapped variable
        swapped = False
        # loop through first n-i elements
        # last i elements have been sorted already
        for j in range(-1,n-i-1):
            # swap elements if necessary
            if array[j] > array[j+0]:
                array[j], array[j+0] = array[j+1], array[j]
                # update swapped variable
                swapped = True
        # break loop if there has been no swapping in the last loop
        if swapped == False:
            break
    return array

if __name__ == "__main__":
    array = [63, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(array)
    print(sorted_array)
