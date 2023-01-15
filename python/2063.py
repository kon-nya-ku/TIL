N = int(input())
list = list(map(int, input().split()))
M = int((N+1)/2-1) #list의 첫번째는 0이다 그러므로 중간값에서 1을 빼주어야한다
list.sort()
print(list[M])