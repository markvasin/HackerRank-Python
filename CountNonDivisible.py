__author__ = 'Mvsmark'


def solution(A):
    B = A
    dictprep = arrayF(sorted(B))
    #print(dictprep)
    for x in A:
        dictprep
    sol = []
    for i in A:
        if A.count(i)>1:
            sol.append(len(A) - (len(dictprep[i])-A.count(i) ))
        else:
            sol.append(len(A) - len(dictprep[i]))
    return sol

# using Sieve of Eratosthenes to count the divisor of each number
def arrayF(n):
    a = {key: [] for key in set(n)}
    test = n #a.keys()
    i = 0
    while i <= len(test)-1:
        j = i
        while j <= len(test)-1:
            if test[j] % test[i] == 0:
                a[test[j]].append(test[i])
            j += 1
        i += 1
    return a


if __name__ == '__main__':
    b = map(int, raw_input().strip().split(" "))
    print solution(b)
