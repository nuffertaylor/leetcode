package completed.java;
import java.util.HashSet;

import completed.java.tools.InputReader;

public class Cd {
  public static void main(String[] args) throws Exception {
    InputReader sc = new InputReader(System.in);
      while (true) {
          int n = sc.nextInt();
          int m = sc.nextInt();

          if (n == 0 && m == 0) break;
          HashSet<Integer> jack = new HashSet<>();
          for (int i = 0; i < n; ++i)
              jack.add(sc.nextInt());

          int ans = 0;
          for (int i = 0; i < m; ++i)
              if (jack.contains(sc.nextInt())) ans++;

          System.out.println(ans);
      }
    sc.close();
  }
}