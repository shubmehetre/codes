package DavidBanas;

import java.util.HashMap;

interface Interfaces2 {
    int x =10;
    default void showName(){
        System.out.println("name is Interfaces2");
    }
}

interface Interfaces1 {
    default void showName(){
        System.out.println("name is Interfaces1");
    }
}

class GoHome implements Interfaces1, Interfaces2{
    @Override
    public void showName() {
        Interfaces1.super.showName(); // Multiple inheritance of implementation
    }
    public int x = 10;
    public static void main(String[] args) {
        GoHome g1 = new GoHome();
        g1.showName();
        System.out.println("value of x in interface 2 is: " + g1.x); // multiple inheritance of type
    }
}