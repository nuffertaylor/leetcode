package completed.java;
import java.util.Scanner;

public class Statues {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int res = Statues.log2(n);
    System.out.println(res+1);
    sc.close();
  }

  public static int log2(int N){
    double result = (Math.ceil(Math.log(N) / Math.log(2)));
    return (int) result;
  }
}
