import sys
input=sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.child = [None]*26
        self.childnum=0
        self.check=False

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        tmp = self.root
        for i in word:
            if tmp.child[ord(i)-97] != None: 
                tmp = tmp.child[ord(i)-97]
            else:
                new = Node(ord(i)-97)
                tmp.child[ord(i)-97] = new
                tmp.childnum+=1
                tmp = new
        tmp.check=True

    def count(self, word):
        #첫 번째 글자는 무조건 입력해야 함.
        tmp = self.root.child[ord(word[0])-97]
        cnt=1
        flag=False
        for i in range(1,len(word)):
            if tmp.childnum==1:
                if not tmp.check:
                    pass
                else:
                    cnt+=1
            else:
                cnt+=1
                
            tmp = tmp.child[ord(word[i])-97]
        return cnt
    
while True:
    try:
        n = int(input())
    except:
        break
    W=[input().rstrip() for i in range(n)]
    trie = Trie()
    Avg=0
    for i in W:
        trie.insert(i)
    for i in W:
        Avg+=trie.count(i)
    print(f'{Avg/n:.2f}')