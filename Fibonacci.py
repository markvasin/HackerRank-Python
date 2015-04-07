__author__ = 'Mvsmark'

def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in xrange(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

if __name__ == '__main__':
    b = input()
    print fibonacciDynamic(b)