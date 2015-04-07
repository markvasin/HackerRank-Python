__author__ = 'Mvsmark'
def solution(A):
    # write your code in Python 2.7
    if len(A) == 0:
        return 1

    mylist = [0] * (len(A)+2)
    mylist[0] = 1
    for item in A:
        mylist[item]=1
    return mylist.index(0)



if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)
