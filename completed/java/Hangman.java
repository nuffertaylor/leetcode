package completed.java;
import java.util.Scanner;
import java.util.HashSet;

public class Hangman {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String word = sc.nextLine(), guess = sc.nextLine();
    HashSet<Character> set = new HashSet<>();
    for(Character c : word.toCharArray())
      set.add(c);
    int incorrectGuesses = 0;
    for(int i=0;i<guess.length();i++)
      if(incorrectGuesses > 9)
        break;
      else if(set.contains(Character.valueOf(guess.charAt(i))))
        set.remove(Character.valueOf(guess.charAt(i)));
      else
        incorrectGuesses++;
    if(set.size() > 0)
      System.out.println("LOSE");
    else
      System.out.println("WIN");
    sc.close();
  }
}