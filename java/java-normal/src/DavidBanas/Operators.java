package DavidBanas;
import java.util.Scanner;

public class Operators {

    public static void main(String[] args) {


/*
        if ((true) && (false)){
            System.out.println("got IN");
        }else {
            System.out.println("got OUT");
        }
*/

/*
        String ss = "";
        if (ss == null){
            System.out.println("inside");
        }else System.out.println("Outside");
*/

/*
        // ternary operator
        String zz = "";
        String zzz = (zz.isEmpty()) ? "String is empty" : "String is not empty";
        System.out.println(zzz);
*/

        Scanner sc = new Scanner(System.in);
        System.out.print("What grade did you get? ");

        // ref: https://stackoverflow.com/questions/13942701/take-a-char-input-from-the-scanner
        char myGrade2 = sc.next(".").charAt(0);

        char myGrade = sc.next().charAt(0);
        char myGrade3 = sc.findInLine(".").charAt(0);

/*
        System.out.println(myGrade);
        System.out.println(myGrade2);
*/
        System.out.println(myGrade3);

/*
        Scanner sc = new Scanner(System.in);
        System.out.print("What grade did you get? ");
        char myGrade = sc.next().charAt(0);

        switch (myGrade){
            case 'a':
                System.out.println("you get cake");
                break;
            case 'b':
                System.out.println("you get soup");
                break;
            case 'c':
                System.out.println("you get veggies dumbfuc");
                break;
            default:
                System.out.println("you know nothin jon snow");
        }
*/

    }

    // called in Variablers class for test purpose
    public static void testPro(){
        System.out.println("this line is from testPro");

    }

}

