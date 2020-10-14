def valid(img,x,y):
    if (x<len(img) and y<len(img[0]) and x>=0 and y>=0):
        return True
    return False




def bfs(img,vis,x,y):
    global clus_front,clus_back;
    global next_clus_back,next_clus_front
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = []
    if (img[x][y]==255):
        vis[x][y] = -1*next_clus_back
        next_clus_back+= 1
        clus_back.append([(x,y)])
    else :
        vis[x][y] = next_clus_front
        next_clus_front+= 1
        clus_front.append([(x,y)])
        
    q.append((x,y))
    
    while(q):
        
        pix = q.pop(0)
        u = pix[0]
        v = pix[1]
        for i in range(4):
            if ( valid(img,u+dx[i],v+dy[i])==True and vis[u+dx[i]][v+dy[i]]==0  ):
                if (img[u][v] == img[u+dx[i]][v+dy[i]]):
                    vis[u+dx[i]][v+dy[i]] = vis[u][v]
                    if (img[u][v]==255):
                        clus_back[-1*vis[u][v]].append((u+dx[i],v+dy[i]))
                    else :
                        clus_front[vis[u][v]].append((u+dx[i],v+dy[i]))
                    q.append((u+dx[i],v+dy[i]))
               
                    
    return vis

def merge(img,vis):
    global clus_front,clus_back;
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    L1 = [(len(clus_front[i]),i ) for i in range(len(clus_front)) ]
    L2 = [(len(clus_back[i]),i ) for i in range(len(clus_back)) ]
    
    cluster1 = max(L1)[1]
    cluster2 = max(L2)[1]
    
    
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (vis[i][j]<0 and vis[i][j]!=(-1*cluster2)):
                img[i][j] = 0
            if (vis[i][j]>0 and vis[i][j]!=(cluster1)):
                img[i][j] = 255
    return img

    
def cluster(img,vis):
    
    for i in range(0,len(img)):
        for j in range(len(img[0])):
            if (vis[i][j]==0):
                bfs(img,vis,i,j)
    return merge(img,vis)
           