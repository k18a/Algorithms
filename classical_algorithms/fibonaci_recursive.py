"""
Function to calculate fibonaci number using a recursive technique. 
Fibonaci number is given as:
\(F(n) = F(n-1) + F(n-2)\)
"""
# initialize base case for 0 and 1 with memoization
memo = {0:0,1:1}

def fibonaci_recursive(n, verbose = False):
    verboseprint = print if verbose else lambda *a, **k: None
    # if value is not in memo
    if n not in memo:
        verboseprint('calculating fibonaci number at {} through recursion to {} and {}'.format(n,n-1,n-2))
        # fibonaci number is given as
        memo[n] = fibonaci_recursive(n-1,verbose) + fibonaci_recursive(n-2,verbose)
    else:
        verboseprint('recursive call to calculate {}th fibonaci number saved due to memoization'.format(n))
    return memo[n]

if __name__ == "__main__":
    fibonaci_recursive(5, verbose=True)
    print('calculated fibonaci numbers are {}'.format(memo))

"""
output:
calculating fibonaci number at 5 through recursion to 4 and 3
calculating fibonaci number at 4 through recursion to 3 and 2
calculating fibonaci number at 3 through recursion to 2 and 1
calculating fibonaci number at 2 through recursion to 1 and 0
recursive call to calculate 1th fibonaci number saved due to memoization
recursive call to calculate 0th fibonaci number saved due to memoization
recursive call to calculate 1th fibonaci number saved due to memoization
recursive call to calculate 2th fibonaci number saved due to memoization
recursive call to calculate 3th fibonaci number saved due to memoization
calculated fibonaci numbers are {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
"""