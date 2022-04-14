x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
u1,v1=x2-x1,y2-y1
u2,v2=x3-x1,y3-y1
ccw=u1*v2-u2*v1
if ccw>0:
    print(1)
elif ccw<0:
    print(-1)
else:
    print(0)