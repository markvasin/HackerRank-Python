__author__ = 'Mvsmark'

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    num = map(int, raw_input().strip().split(" "))
    print(gcd(num[0],num[1]))