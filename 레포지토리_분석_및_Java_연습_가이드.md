# 알고리즘 문제풀이 레포지토리 분석 및 Java 연습 가이드

## 📋 레포지토리 분석 결과

### 구조 개요
- **총 Python 파일 개수**: 141개
- **주요 플랫폼**: 백준(BOJ), 프로그래머스, SWEA
- **난이도 분포**: 
  - 백준: Bronze, Silver, Gold, Platinum
  - 프로그래머스: Level 1-4, Unrated
  - SWEA: D3

### 주요 알고리즘 유형
1. **그래프 탐색** (DFS/BFS)
2. **분할정복** (Z 문제 등)
3. **동적 프로그래밍** (피보나치, 이항계수 등)
4. **문자열 처리** (다트 게임, 괄호 문제 등)
5. **백트래킹** (순열, 조합 문제)
6. **수학** (기하학, 수론 문제)

## 🔄 Python → Java 변환 연습 가이드

### 1. 기본 입출력 변환

#### Python
```python
# 한 줄 입력
n = int(input())

# 여러 개 입력
a, b = map(int, input().split())

# 리스트 입력
arr = list(map(int, input().split()))

# 빠른 입력 (sys.stdin.readline)
import sys
input = sys.stdin.readline
```

#### Java
```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        // 한 줄 입력
        int n = Integer.parseInt(br.readLine());
        
        // 여러 개 입력
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        
        // 배열 입력
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }
}
```

### 2. 자주 사용되는 자료구조 변환

#### Python → Java
| Python | Java |
|--------|------|
| `list()` | `ArrayList<>()` |
| `deque()` | `ArrayDeque<>()` |
| `set()` | `HashSet<>()` |
| `dict()` | `HashMap<>()` |
| `heapq` | `PriorityQueue<>()` |

### 3. 대표 문제별 Java 변환 예시

#### 예시 1: 터렛 문제 (백준 1002)
**Python 코드:**
```python
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == distance or (r1+r2) == distance:
        print(1)
    elif abs(r1-r2) < distance < (r1+r2):
        print(2)
    else:
        print(0)
```

**Java 변환:**
```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            
            double distance = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));
            
            if (distance == 0 && r1 == r2) {
                System.out.println(-1);
            } else if (Math.abs(r1-r2) == distance || (r1+r2) == distance) {
                System.out.println(1);
            } else if (Math.abs(r1-r2) < distance && distance < (r1+r2)) {
                System.out.println(2);
            } else {
                System.out.println(0);
            }
        }
    }
}
```

#### 예시 2: 올바른 괄호 (프로그래머스 lv2)
**Python 코드:**
```python
def solution(s):
    answer = True
    l_cnt = 0
    
    for i in s:
        if l_cnt < 0:
            return False
        if i == "(":
            l_cnt += 1
        else:
            l_cnt -= 1
    
    if l_cnt:
        return False
    return True
```

**Java 변환:**
```java
class Solution {
    boolean solution(String s) {
        int l_cnt = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (l_cnt < 0) {
                return false;
            }
            if (c == '(') {
                l_cnt++;
            } else {
                l_cnt--;
            }
        }
        
        return l_cnt == 0;
    }
}
```

## 🎯 연습 순서 추천

### 1단계: 기본 문제 (Bronze/Level 1)
- 입출력 처리 익히기
- 기본 자료구조 사용법 익히기
- 조건문, 반복문 변환 연습

### 2단계: 중급 문제 (Silver/Level 2)
- 배열, 문자열 처리
- 수학적 계산 문제
- 간단한 그래프 문제

### 3단계: 고급 문제 (Gold/Level 3-4)
- 복잡한 알고리즘 구현
- 자료구조 활용 문제
- 최적화 문제

## 🔧 Java 개발 환경 설정

### 필요한 import 문
```java
import java.util.*;
import java.io.*;
```

### 기본 템플릿
```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        // 여기에 코드 작성
        
        br.close();
    }
}
```

## 📚 주요 차이점 정리

### Python vs Java
| 항목 | Python | Java |
|------|--------|------|
| 변수 선언 | `x = 10` | `int x = 10;` |
| 배열 크기 | `len(arr)` | `arr.length` |
| 문자열 길이 | `len(s)` | `s.length()` |
| 제곱근 | `x ** 0.5` | `Math.sqrt(x)` |
| 절댓값 | `abs(x)` | `Math.abs(x)` |
| 최대/최소 | `max()`, `min()` | `Math.max()`, `Math.min()` |

## 🎯 실습 권장사항

1. **Python 코드를 먼저 이해**한 후 Java로 변환
2. **한 번에 하나씩** 단계별로 변환
3. **컴파일 에러**를 통해 Java 문법 익히기
4. **성능 최적화**는 나중에 고려 (우선 동작하는 코드 작성)
5. **정해진 시간 내에** 변환 완료를 목표로 설정

이 가이드를 통해 Python으로 작성된 알고리즘 문제들을 Java로 변환하는 연습을 해보세요. 각 문제의 로직은 동일하지만, Java의 문법과 특성을 익히는 좋은 기회가 될 것입니다!