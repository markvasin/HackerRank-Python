__author__ = 'Mvsmark'

def solution(K, L, M, N, P, Q, R, S):
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


    return max(0, (min(B,D) - max(A,C)))

if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))

    print solution(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7])