__author__ = 'Mvsmark'
def solution(A):
    # write your code in Python 2.7
    if len(A) == 0:
        return 1

    mydic = {key:0 for key in xrange(1,len(A)+2)}
    for item in A:
        mydic[item]=1
    return mydic.keys()[mydic.values().index(0)]



if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)
