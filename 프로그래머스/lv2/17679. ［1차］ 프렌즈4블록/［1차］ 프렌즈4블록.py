import traceback
def board_update(m,n,board,check):
    try:
        ans=0
        for i in range(m):
            for j in range(n):
                if check[i][j]==1:
                    board[i][j]=""
                    ans+=1
    except:
        print("update fail1!")
        err_msg = traceback.format_exc()
        print("1", err_msg)
        return 
        
    try:
        for j in range(n):
            empty=[]
            for i in range(m):
                # 빈 방
                if board[m-i-1][j]=="":
                    empty.append([m-i-1,j])
                else:
                    if empty:
                        u,v=empty.pop(0)
                        board[u][v]=board[m-i-1][j]
                        board[m-i-1][j]=""
                        empty.append([m-i-1,j])
    except:
        print("update fail2!")
        err_msg = traceback.format_exc()
        print("2", err_msg)
        return
        
    return board,ans

def solution(m, n, board):
    answer = 0
    dx=[1,0,1]
    dy=[0,1,1]
    
    for i in range(m):
        board[i]=list(board[i])
    try:
        # update를 진행해야하는지 결정
        flag=True
        while flag:
            flag=False
            check=[[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if board[i][j]=="":
                        continue
                    character=board[i][j]
                    #print(character)
                    cnt=0
                    for k in range(3):
                        x=i+dx[k]
                        y=j+dy[k]
                        if x<0 or x>=m or y<0 or y>=n:
                            continue
                        if board[x][y]=="" or board[x][y]!=character:
                            continue
                        cnt+=1

                    if cnt==3:
                        print(i,j)
                        check[i][j]=1
                        for k in range(3):
                            x=i+dx[k]
                            y=j+dy[k]
                            check[x][y]=1
                        flag=True
                        
            board,ans=board_update(m,n,board,check)
            answer+=ans
    except:
        return
    return answer