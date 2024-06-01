def fish_eat():
    check = False
    global eat,shark,ans,er,ec

    now = 10000000
    for row in range(N):
        for col in range(N):
            if 0< arr[row][col] < shark:
                if now>ans[row][col]:
                    er = row
                    ec = col
                    now = ans[row][col]
                    check = True



    eat += 1
    if shark == eat:
        shark += 1
        eat = 0
    arr[er][ec] = 0

    return ans[er][ec] ,er,ec

def can_eat():
    flag = False
    for row in range(N):
        for col in range(N):
            if 0< arr[row][col] < shark:
                flag =True
    return flag

def bfs(sr,sc):
    visited = [[21e9] * N for _ in range(N)]
    global shark
    q = [(sr,sc)]
    visited[sr][sc] = 0

    while q:
        vr,vc = q.pop(0)

        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<N and 0<=newC<N and visited[vr][vc] + 1 < visited[newR][newC]:
                if arr[newR][newC] <= shark:
                    visited[newR][newC] = visited[vr][vc] + 1
                    q.append((newR,newC))
    return visited


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 2
cnt = 0
sr = 0
sc = 0
er =0
ec =0
for row in range(N):
    for col in range(N):
        if arr[row][col] == 9:
            arr[row][col] = 0
            sr = row
            sc = col
eat = 0
time = 0
while True:
    if can_eat() == False:
        break
    ans = bfs(sr,sc)
    t,sr,sc = fish_eat()
    time += t

if time==21e9:
    print(0)
else:
    print(time)