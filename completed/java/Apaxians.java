package completed.java;
import java.util.Scanner;
import java.lang.StringBuilder;

public class Apaxians {
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    StringBuilder sb = new StringBuilder();
    String name = sc.nextLine();
    for(int i = 0; i < name.length(); i++)
      if(i == 0) 
        sb.append(name.charAt(i));
      else if(name.charAt(i) != name.charAt(i-1)) 
        sb.append(name.charAt(i));
    System.out.println(sb.toString());
  }
}