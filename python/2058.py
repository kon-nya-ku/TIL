N = int(input())
if 0< N < 10000:
    def digits(N):
        if N > 0: 
            return N % 10 + digits(N // 10)
        else:
            return 0
    print( digits(N) )
else :
    print('input이 1부터 9999의 자연수가 아닙니다')