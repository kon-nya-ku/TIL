N = int(input())

for i in range(N):
    LM = list(map(int, input().split()))
    M = max(LM)
    print('#{} {}'.format(i, M))

