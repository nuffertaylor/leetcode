package completed.java;
import java.util.Scanner;

public class TrollHunt {
  public static void main(String[] args) throws Exception
  {
    Scanner reader = new Scanner(System.in);
    int b = reader.nextInt()-1, k = reader.nextInt(), g = reader.nextInt();
    int numGroups = k/g;
    if(b%numGroups==0) System.out.println(b/numGroups);
    else System.out.println((b/numGroups)+1);
    reader.close();
  }
}