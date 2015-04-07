__author__ = 'Mvsmark'

def solution(A):
    A.sort()
    for index, i in enumerate(A):
        if(index != len(A)-1):
            if (i + 1 != A[index+1]):
                return 0
    return 1



if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)