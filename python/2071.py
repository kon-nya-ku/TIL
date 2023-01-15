N = int(input())

for t in range(1,N+1) :
    AL = list(map(int, input().split()))
    aver = round( sum(AL) / len (AL) )
    print(f'#{t} {aver}')