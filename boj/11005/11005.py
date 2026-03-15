N,B=map(int,input().split())
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

while N>0:
  ans+=tmp[N%B]
  N//=B

print(ans[::-1])