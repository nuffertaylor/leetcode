package completed.java;
import java.util.Scanner;
import java.util.List;
import java.util.Arrays;
import java.util.Comparator;
import java.lang.StringBuilder;

public class Abc
{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    List<Integer> nums = Arrays.asList(sc.nextInt(), sc.nextInt(), Integer.valueOf(sc.nextLine().trim()));
    nums.sort(Comparator.naturalOrder());
    String order = sc.nextLine();
    StringBuilder answer = new StringBuilder();
    for(char c : order.toCharArray())
    {
      if(answer.length() > 0) 
        answer.append(" ");
      if(c=='A')
        answer.append(nums.get(0));
      else if(c=='B')
        answer.append(nums.get(1));
      else if(c=='C')
        answer.append(nums.get(2));
    }
    System.out.println(answer.toString());
    sc.close();
  }
}
