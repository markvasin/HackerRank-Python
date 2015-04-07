__author__ = 'Mvsmark'
def lonelyinteger(a):
    return min(set(a), key=a.count)

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
