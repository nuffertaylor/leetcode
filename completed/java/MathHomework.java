package completed.java;
import java.util.Scanner;
import java.util.ArrayList;

public class MathHomework {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(), m = sc.nextInt();
    ArrayList<String> results = new ArrayList<>();

    for(int x=0; x<(m/a)+1; x++)
      for(int y=0; y<(m/b)+1; y++)
        for(int z=0; z<(m/c)+1; z++)
          if(((a*x)+(b*y)+(c*z)) == m)
            results.add(String.valueOf(x) + " " + String.valueOf(y) + " " + String.valueOf(z));
    
    if(results.size() == 0)
      System.out.println("impossible");
    else
      for(String s : results)
        System.out.println(s);
  sc.close();
  }
}
