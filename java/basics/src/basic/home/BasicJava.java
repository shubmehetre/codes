package basic.home;

import java.util.Arrays;
import java.util.Scanner;

public class BasicJava {
    BasicJava(){}

    public void kmconvert()
    {

        System.out.println("What u wanna do? Press 1/2");
        System.out.println("1. km --> miles\n2. miles --> km");

        Scanner sc = new Scanner(System.in);
        String choice = sc.nextLine();

        switch (choice) {
            case "1" -> {
                System.out.print("km = ");
                float km = sc.nextFloat();
                System.out.println("miles = " + (float) (km / 1.6));
            }
            case "2" -> {
                System.out.print("miles = ");
                float miles = sc.nextFloat();
                System.out.println("kilometers = " + (float) (miles * 1.6));
            }
        }
    }

    public static void main(String [] args)
    {
        BasicJava seed = new BasicJava();

        // km to miles converter
         seed.kmconvert();

    }
}
