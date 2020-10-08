""" 
given a array of numbers, sort them so even elements appear first
"""
def sort_even_odd(array):
    # initialize next_even and next_odd indices
    next_even, next_odd = 0, len(array) - 1
    # while next_even indice is less than next odd indice
    while next_even < next_odd:
        # check if the number on the even indice is even
        if ~ array[next_even] & 1:
            # increment next even
            next_even += 1
        # if number in odd indice is odd
        elif array[next_odd] & 1:
            # decrement next odd
            next_odd -= 1
        # otherwise
        else:
            # swap places
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            # change indices
            next_even += 1
            next_odd -= 1
    return array

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9]
    sorted_array = sort_even_odd(array)
    print(sorted_array)