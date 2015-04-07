__author__ = 'Mvsmark'


def solution(A):

    if len(A) == 0:
        return 1
    elif len(A) == 1:
        if A[0] == 1:
            return 2
        else:
            return 1

    B = [item for item in A if item >= 0]

    if len(B) == 0:
        return 1
    if len(B) == 1:
        if B[0] == 1:
            return 2
        else:
            return 1

    B.sort()
    if B[0] != 0 and B[0] != 1:
        return 1
    for index, i in enumerate(B):
        if index != len(B) - 1:
            if i != B[index + 1]:
                if i + 1 != B[index + 1]:
                    return i + 1
    return B[len(B)-1] + 1


if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)