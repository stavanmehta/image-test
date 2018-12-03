
def solution(N):
    # write your code in Python 3.6
    commands = list()
    L = 0
    R = 1

    def getL():
        return 2 * L - R

    def getR():
        return 2 * R - L

    print L
    if N < 0:
        L = getL()
        commands.append(L)

        while L >= N:
            L = getL()
            if L + R - N == 0:
                R = getR()
            commands.append(L)
        print commands



if __name__ == '__main__':
    solution(-11)