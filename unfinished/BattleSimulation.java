package unfinished;
import java.util.Scanner;
import java.lang.StringBuilder;

public class BattleSimulation {
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    String godzilla = sc.nextLine();
    sc.close();
    StringBuilder mech = new StringBuilder();
    for(int i = 0; i < godzilla.length(); i++)
    {
      if(i<godzilla.length()-3)
      {
        if(isCombo(godzilla.substring(i, i+3)))
        {
          mech.append('C');
          i = i+2;
        }
        else {mech.append(getLetter(godzilla.charAt(i)));}
      }
      else {mech.append(getLetter(godzilla.charAt(i)));}
    }
    System.out.println(mech.toString());
  }

  public static boolean isCombo(String moves)
  {
    if(moves.contains("L") && moves.contains("B") && moves.contains("R"))
      return true;
    return false;
  }

  public static char getLetter(char c)
  {
    if(c == 'L')
      return 'H';
    else if(c == 'B')
      return 'K';
    else if(c == 'R')
      return 'S';
    else
      return 'F'; //for failure
  }
}
