package DavidBanas;

public interface Tester {
    int x = 10;

    static void getName(){
        System.out.println("my name raul");
    }
    default void getID(){
        System.out.println("my id is 101");
    }
}