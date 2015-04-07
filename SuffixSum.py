__author__ = 'Mvsmark'

def solution(A):
    sufsum = suffix_sums(A)
    count = 0
    for index, val in enumerate(A):
        if val == 0:
            count += sufsum[index]
        if count > 1000000000:
            return -1
    return count

# suffix sum algorithm
def suffix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(n-1, -1, -1):
        P[k] = P[k + 1] + A[k]
    return P

if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)