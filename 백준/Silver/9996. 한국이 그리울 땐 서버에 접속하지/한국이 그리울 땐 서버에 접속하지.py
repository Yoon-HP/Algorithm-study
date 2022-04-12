N=int(input())
key=input()
for _ in range(N):
    check=input()
    if len(key)-1>len(check):
        print("NE")
    else:
        for i in range(len(key)):
            if key[i]=="*":
                cnt=len(key[i+1:])
                if key[i+1:]==check[-cnt:]:
                    print("DA")
                    break
                else:
                    print("NE")
                    break
            else:
                if key[i]!=check[i]:
                    print("NE")
                    break   