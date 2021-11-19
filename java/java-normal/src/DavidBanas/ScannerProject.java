package DavidBanas;
/*
  Author: Shubham A. Mehetre
  Project: Guessing game
  Purpose: Scanner Practice
 */

import java.util.Random;
import java.util.Scanner;

public class ScannerProject {
    static double randNum = randNumGenerator();

    public static int randNumGenerator() {
        randNum = (int) (Math.random() * 11);
        return (int) randNum;
    }

    public static int inputTaker(int tries) {
        System.out.print("guess num from 0-10: ");
        Scanner sc = new Scanner(System.in);
        int userInput;
        if (sc.hasNextInt()) {
            userInput = sc.nextInt();
        } else {
            System.out.println("Do u call that a number??!");
            System.out.println(tries + " tries left");
            return inputTaker(tries);
        }
        return userInput;
    }

    public static int guessCheck(int guess) {
        if (guess == randNum) {
            System.out.println("YOU WON!");
            return -1;
        }
        else
            return guess;
    }

    public static void introText(){
        System.out.print("-------------GUESSING GAME------------------\n");
        System.out.println("Guess the number! its between 0 and 10\nYou got 3 tries\n");
    }
    public static void main(String[] args) {
        introText();

        int guessValue = 0;
        int guessResult = 0;
        int tries = 3;

        while (guessResult != -1){
            System.out.println(tries + " tries left");
            guessValue = inputTaker(tries);
            guessResult = guessCheck(guessValue);
            tries--;
            if(tries==0){
                System.out.println("Go home");
                break;
            }
        }
    }
}