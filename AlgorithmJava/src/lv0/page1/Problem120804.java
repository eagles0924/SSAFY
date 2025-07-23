package lv0.page1;

public class Problem120804 {
  public int solution(int num1, int num2) {
    int answer;
    answer = num1 * num2;
    return answer;
  }
  public static void main(String[] args) {
      Problem120804 p = new Problem120804();  //앞의 패키지 쓸 필요없음.
      int result = p.solution(3, 4);
      System.out.println("결과: " + result);
  }
}
