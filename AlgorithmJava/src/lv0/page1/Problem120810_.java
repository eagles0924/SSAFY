package lv0.page1;

public class Problem120810_ {
  public int solution(int num1, int num2) {
    int answer;
    answer = num1 % num2;
    return answer;
  }
  public static void main(String[] args) {
      Problem120810_ p = new Problem120810_();
      int result = p.solution(10,6);
      System.out.println("결과: " + result);
  }
}
