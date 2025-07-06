# Java 변환 연습 문제집

## 📝 연습 문제 목록

### 1. 기본 입출력 연습 (난이도: ★☆☆☆☆)

#### 문제 1: Z 문제 (백준 1074)
**Python 코드:**
```python
N, r, c = map(int, input().split())
ans = 0
# 결국 r,c를 0,0으로 옮기는 과정을 거쳐가며 개수를 세면 됨.
# 1/4로 주어진 table을 계속해서 분할해 가면서 답을 찾아 나감.
# 규칙을 찾고 이를 일반화해서 표현 하면 됨.
while N != 0:
    N -= 1
    if r < 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 0
    elif r < 2**N and c >= 2**N:
        ans += (2**N) * (2**N) * 1
        c -= 2**N
    elif r >= 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 2
        r -= 2**N
    else:
        ans += (2**N) * (2**N) * 3
        r -= 2**N
        c -= 2**N
print(ans)
```

**Java 변환 해보기:**
```java
// 여기에 Java 코드를 작성해보세요
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드 작성
        
    }
}
```

---

### 2. 배열과 반복문 (난이도: ★★☆☆☆)

#### 문제 2: 모든 순열 (백준 10974)
**Python 코드:**
```python
N = int(input())
B = [i+1 for i in range(N)]
s = []

def dfs():
    if len(s) == N:
        print(' '.join(map(str, s)))
        return
    for i in B:
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()
```

**Java 변환 해보기:**
```java
// 여기에 Java 코드를 작성해보세요
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static ArrayList<Integer> s = new ArrayList<>();
    
    public static void main(String[] args) throws IOException {
        // 여기에 코드 작성
        
    }
    
    static void dfs() {
        // 여기에 코드 작성
        
    }
}
```

---

### 3. 문자열 처리 (난이도: ★★☆☆☆)

#### 문제 3: 다트 게임 (프로그래머스 lv1)
**Python 코드:**
```python
import re

def solution(dartResult):
    answer = 0
    
    rule = {'S': 1, 'D': 2, 'T': 3}
    score = re.findall(r'[0-9]+', dartResult)
    bonus = re.findall(r'[a-zA-Z]', dartResult)
    option = ['', '', '']
    
    cnt = -1
    for i in dartResult:
        if i.isalpha():
            cnt += 1
            continue
        if i.isdigit():
            continue
        if i == '*' or i == '#':
            option[cnt] = i
    
    for i in range(3):
        if option[i] == '*':
            score[i] = int(score[i]) ** rule[bonus[i]] * 2
            if i != 0:
                score[i-1] *= 2
        elif option[i] == '#':
            score[i] = (int(score[i]) ** rule[bonus[i]]) * (-1)
        else:
            score[i] = int(score[i]) ** rule[bonus[i]]
    
    answer = sum(score)
    return answer
```

**Java 변환 해보기:**
```java
// 여기에 Java 코드를 작성해보세요
import java.util.*;
import java.util.regex.*;

class Solution {
    public int solution(String dartResult) {
        // 여기에 코드 작성
        
        return 0;
    }
}
```

---

### 4. 그래프 탐색 (난이도: ★★★☆☆)

#### 문제 4: 적록색약 (백준 10026)
**Python 코드:**
```python
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
table = [list(input()) for i in range(N)]
visited = [[False]*N for i in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q = deque([[j, i]])
            color = table[i][j]
            visited[i][j] = True
            cnt += 1
            
            while q:
                x, y = q.popleft()
                for k in range(4):
                    a, b = x + dx[k], y + dy[k]
                    if 0 <= a < N and 0 <= b < N and not visited[b][a] and table[b][a] == color:
                        visited[b][a] = True
                        q.append([a, b])

print(cnt)
```

**Java 변환 해보기:**
```java
// 여기에 Java 코드를 작성해보세요
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static char[][] table;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    
    public static void main(String[] args) throws IOException {
        // 여기에 코드 작성
        
    }
}
```

---

## 💡 정답 및 해설

### 문제 1 정답
```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        
        int ans = 0;
        
        while (N != 0) {
            N--;
            int size = (int) Math.pow(2, N);
            
            if (r < size && c < size) {
                ans += size * size * 0;
            } else if (r < size && c >= size) {
                ans += size * size * 1;
                c -= size;
            } else if (r >= size && c < size) {
                ans += size * size * 2;
                r -= size;
            } else {
                ans += size * size * 3;
                r -= size;
                c -= size;
            }
        }
        
        System.out.println(ans);
    }
}
```

### 문제 2 정답
```java
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static ArrayList<Integer> s = new ArrayList<>();
    static boolean[] used;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        used = new boolean[N + 1];
        
        dfs();
    }
    
    static void dfs() {
        if (s.size() == N) {
            for (int i = 0; i < s.size(); i++) {
                System.out.print(s.get(i));
                if (i < s.size() - 1) System.out.print(" ");
            }
            System.out.println();
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (!used[i]) {
                s.add(i);
                used[i] = true;
                dfs();
                s.remove(s.size() - 1);
                used[i] = false;
            }
        }
    }
}
```

### 문제 3 정답
```java
import java.util.*;
import java.util.regex.*;

class Solution {
    public int solution(String dartResult) {
        Map<Character, Integer> rule = new HashMap<>();
        rule.put('S', 1);
        rule.put('D', 2);
        rule.put('T', 3);
        
        Pattern scorePattern = Pattern.compile("[0-9]+");
        Pattern bonusPattern = Pattern.compile("[a-zA-Z]");
        
        Matcher scoreMatcher = scorePattern.matcher(dartResult);
        Matcher bonusMatcher = bonusPattern.matcher(dartResult);
        
        ArrayList<Integer> scores = new ArrayList<>();
        ArrayList<Character> bonuses = new ArrayList<>();
        
        while (scoreMatcher.find()) {
            scores.add(Integer.parseInt(scoreMatcher.group()));
        }
        
        while (bonusMatcher.find()) {
            bonuses.add(bonusMatcher.group().charAt(0));
        }
        
        String[] options = {"", "", ""};
        int cnt = -1;
        
        for (int i = 0; i < dartResult.length(); i++) {
            char c = dartResult.charAt(i);
            if (Character.isLetter(c)) {
                cnt++;
                continue;
            }
            if (Character.isDigit(c)) {
                continue;
            }
            if (c == '*' || c == '#') {
                options[cnt] = String.valueOf(c);
            }
        }
        
        int[] finalScores = new int[3];
        
        for (int i = 0; i < 3; i++) {
            int score = (int) Math.pow(scores.get(i), rule.get(bonuses.get(i)));
            
            if (options[i].equals("*")) {
                score *= 2;
                if (i != 0) {
                    finalScores[i-1] *= 2;
                }
            } else if (options[i].equals("#")) {
                score *= -1;
            }
            
            finalScores[i] = score;
        }
        
        return Arrays.stream(finalScores).sum();
    }
}
```

### 문제 4 정답
```java
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static char[][] table;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        
        table = new char[N][N];
        visited = new boolean[N][N];
        
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                table[i][j] = line.charAt(j);
            }
        }
        
        int cnt = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, table[i][j]);
                    cnt++;
                }
            }
        }
        
        System.out.println(cnt);
    }
    
    static void bfs(int startY, int startX, char color) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{startX, startY});
        visited[startY][startX] = true;
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && 
                    !visited[ny][nx] && table[ny][nx] == color) {
                    visited[ny][nx] = true;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }
    }
}
```

## 📋 체크리스트

### 완료한 문제 체크
- [ ] 문제 1: Z 문제 (분할정복)
- [ ] 문제 2: 모든 순열 (백트래킹)
- [ ] 문제 3: 다트 게임 (문자열 처리)
- [ ] 문제 4: 적록색약 (BFS)

### 다음 단계 추천
1. **더 많은 문제 변환**: 레포지토리의 다른 Python 코드들을 Java로 변환해보세요
2. **최적화 연습**: 동일한 기능을 더 효율적으로 구현해보세요
3. **새로운 알고리즘**: 레포지토리에 없는 새로운 알고리즘을 Java로 구현해보세요

---

**💪 연습 팁**: 
- 먼저 Python 코드의 로직을 완전히 이해하고 시작하세요
- Java 문법에 익숙해질 때까지 반복 연습하세요
- 컴파일 에러는 학습의 기회입니다 - 에러 메시지를 통해 Java의 특성을 익히세요!