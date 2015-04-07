__author__ = 'Mvsmark'

def solution(A):
    if A < 1:
        return 0
    val1 = largestdivider(A)
    return 2 * (val1 + (A/val1))

def largestdivider(n):
    i = 1
    sol = 0
    while i * i <= n:
        if n % i == 0:
            if sol < i:
                sol = i
        i += 1
    return sol


if __name__ == '__main__':
    b = input()
    print solution(b)