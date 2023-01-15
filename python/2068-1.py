N = int(input())

for i in range(1,N+1):
    LM = map(int, input().split())
    M = max(LM)
    print(f'#{i} {M}')