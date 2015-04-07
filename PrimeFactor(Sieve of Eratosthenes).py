__author__ = 'Mvsmark'

def primefactor(num):
    arrayPrep = arrayF(num)
    print arrayPrep
    return factorization(num, arrayPrep)

def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while (i * i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i
                k += i
        i += 1
    return F

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x /= F[x]
    primeFactors += [x]
    return primeFactors

if __name__ == '__main__':
    print primefactor(input("Please input a number: "))