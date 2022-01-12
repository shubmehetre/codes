//
package DavidBanas;
// Adding books to home library

import java.util.Scanner;

public class HomeLibrary {
    static int id = 101;

    HomeLibrary(){
        System.out.println("\nNow Constructor" +"\nHi From in CONSTRUCTOR\n");
    }

    public static void main(String[] args) {
        HomeLibrary h1 = new HomeLibrary();
        System.out.println("Now in main" + "\nHi from MAIN method");
    }

    static {
        System.out.println("Hi from STATIC INIT BLOCK");
        System.out.println("class variable id is: " + id + "\nStill in static init block");
    }
}
