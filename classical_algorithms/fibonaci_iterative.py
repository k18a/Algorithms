"""
Function to calculate fibonaci number using a recursive technique. 
Fibonaci number is given as:
\(F(n) = F(n-1) + F(n-2)\)
"""
def fibonaci_iterative(n, verbose=False):
    verboseprint = print if verbose else lambda *a, **k: None
    # initialize first 2 numbers
    previous_number, current_number = 0, 1
    verboseprint('{}th number is {}'.format(1, 0))
    # iterate n times
    for _ in range(1,n):
        ' fibonaci number is given as'
        previous_number, current_number = \
            current_number, previous_number + current_number
        verboseprint('{}th number is {}'.format(_+1, current_number))
    return current_number

if __name__ == "__main__":
    fibonaci_iterative(15,verbose=True)
"""
output:
1th number is 0
2th number is 1
3th number is 2
4th number is 3
5th number is 5
6th number is 8
7th number is 13
8th number is 21
9th number is 34
10th number is 55
11th number is 89
12th number is 144
13th number is 233
14th number is 377
15th number is 610
"""