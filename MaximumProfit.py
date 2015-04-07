__author__ = 'Mvsmark'

def solution(A):
    return golden_max_slice(prefix_subtract(A))

# prefix subtract algorithm

def prefix_subtract(A):
    n = len(A)
    P = [0] * n
    for k in xrange(0, n):
        if k != n-1:
            P[k] = A[k + 1] - A[k]
    return P


# maximun slice algorithm
def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)
