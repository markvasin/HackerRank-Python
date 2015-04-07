def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 2.7
    rect1 = (M-K) * (N-L)
    rect2 = (R-P) * (S-Q)
    interceptWidth = getinterceptLength(K,M,P,R)
    interceptHeight = getinterceptLength(L,N,Q,S)
    sum = rect1 + rect2 - (interceptWidth * interceptHeight)
    if sum > 2147483647:
        return -1
    else:
        return sum


def getinterceptLength(A,B,C,D):
    len = min(B,D) - max(A,C)
    if len < 0:
        return 0
    else:
        return len