""""
radix sort
"""
from sort_counting import counting_sort

def radix_sort(array):
    # get array maximum
    maximum = max(array)
    # initialize exponent
    exponent = 1

    # check if exponent is greater than max
    while exponent < maximum:
        # count sort array for the given exponent
        counting_sort(array,inplace=True,exponent=exponent)
        # multiply exponent by 10
        exponent *= 10
    
    return array

if __name__ == "__main__":
    array = [170,45,90,802,24,2,66]
    radix_sort(array)
    print(array)