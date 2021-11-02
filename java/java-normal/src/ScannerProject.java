/*
  Author: Shubham A. Mehetre
  Project: Guessing game
  Purpose: Scanner Practice
 */

import java.util.Random;
import java.util.Scanner;

public class ScannerProject {

    public int inputTaker() {
        Scanner sc = new Scanner(System.in);
        System.out.print("type here: ");
        int x = 0;
        if (sc.hasNextInt()) {
            x =  sc.nextInt();
        } else {
            System.out.println("Pls enter a number");
            inputTaker();
        }
        return x;
    }

    public static void main(String[] args) {
        ScannerProject obj = new ScannerProject();

        System.out.print("-------------GUESSING GAME------------------\n");
        System.out.println("Guess the number! its between 1 and 10\nYou got 3 tries\n");

        Random r = new Random();
        int randNum = r.nextInt(11);
        System.out.println(randNum);

        for (int i = 3; i > 0; i--) {
            int userInput = obj.inputTaker();
            if (userInput == randNum) {
                System.out.println("!!!!!!!!!YOU WON!!!!!!!!!!\n");
                break;
            }
            else if (i == 1)
                System.out.println("You Lose");
            else
                System.out.println((i - 1) + " tries left");
        }
    }
}


