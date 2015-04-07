__author__ = 'Mvsmark'

# using stack
def solution(S):
    matched = {"]":"[", "}":"{", ")": "("}
    to_push = ["[", "{", "("]
    stack = []

    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif matched[element] != stack.pop():
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    mystring = raw_input()
    print(solution(mystring))