text=input()

check=0
target=["U","C","P","C"]
for i in text:
    if check==4:
        break
    if i==target[check]:
        check+=1
        
if check==4:
    print("I love UCPC")
else:
    print("I hate UCPC")