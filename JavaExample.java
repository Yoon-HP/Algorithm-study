import java.util.*;
import java.io.*;

// 터렛 문제 (백준 1002) - Python에서 Java로 변환 예시
public class JavaExample {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        System.out.println("터렛 문제 테스트");
        System.out.println("테스트 케이스 개수를 입력하세요:");
        
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < T; t++) {
            System.out.println("x1 y1 r1 x2 y2 r2를 입력하세요:");
            st = new StringTokenizer(br.readLine());
            
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            
            double distance = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));
            
            if (distance == 0 && r1 == r2) {
                System.out.println("결과: -1 (무한대)");
            } else if (Math.abs(r1-r2) == distance || (r1+r2) == distance) {
                System.out.println("결과: 1 (한 점에서 만남)");
            } else if (Math.abs(r1-r2) < distance && distance < (r1+r2)) {
                System.out.println("결과: 2 (두 점에서 만남)");
            } else {
                System.out.println("결과: 0 (만나지 않음)");
            }
        }
        
        br.close();
        System.out.println("프로그램이 종료되었습니다.");
    }
}