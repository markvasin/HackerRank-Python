__author__ = 'Mvsmark'

def solution(A):
    # write your code in Python 2.7
    listcount = counting(A, max(A))
    listcount[0] = 1
    if 0 not in listcount:
        return 1
    else:
        return 0

# use list to cout the element
def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in xrange(n):
        count[A[k]] += 1
    return count

if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)