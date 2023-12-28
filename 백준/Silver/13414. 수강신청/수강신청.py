# 13414번 수강신청
import sys
input=sys.stdin.readline

K,L=map(int,input().split())

Student_dict={}

for i in range(L):
    no=input().strip()
    if no not in Student_dict:
        Student_dict[no]=i
    else:
        Student_dict[no]=i

Success=[]

for i in Student_dict.keys():
    Success.append([Student_dict[i],i])

Success.sort()

for i in range(min(K,len(Success))):
    print(Success[i][1])
