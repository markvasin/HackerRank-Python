__author__ = 'Mvsmark'

def solution(A, B, K):
    # write your code in Python 2.7
    if A%K != 0:
        return (B//K)-(A//K) + 1
    else:
        return (B//K)-(A//K)