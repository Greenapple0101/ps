T = int(input())
for test_case in range(1, T + 1):
    N,K=map(int,input().split())
    ans=0
    visited=[0]*13
    def dfs(n,k,start):
        global ans,visited
        if(n==N):
            if(k==K):
                ans+=1
                return
            else:
                return

        for i in range(start,12):
            if(visited[i+1]):continue
            visited[i+1]=1
            dfs(n+1,k+i+1,i+1)
            visited[i+1]=0

    dfs(0,0,0)
    print(f"#{test_case} {ans}")