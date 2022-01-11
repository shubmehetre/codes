package DavidBanas;
// Adding books to home library

import java.util.Scanner;

public class HomeLibrary {
    private int bookID;
    private String bookName;
    private static int totalBookCount = 0;

    HomeLibrary( int bookID, String bookName ){
        this.bookID = bookID;
        this.bookName = bookName;
        totalBookCount++;
    }

    HomeLibrary(){
        System.out.println("Pass Id and name when creating objects");
    }

    public static void main(String[] args) {
        HomeLibrary homer1 = new HomeLibrary(101 ,"Illiyad by Homer");
        HomeLibrary homer2 = new HomeLibrary(101 ,"Odyssee by Homer");
        HomeLibrary orwell = new HomeLibrary(101 ,"Animal Farm");
        HomeLibrary tester = new HomeLibrary();

        System.out.println("Total books added are " + HomeLibrary.totalBookCount);
    }
}
