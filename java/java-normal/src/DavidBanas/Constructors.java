package DavidBanas;

import java.util.Arrays;

public class Constructors<x> {

    public int x = 10;
    public int y = 5;

    Constructors(int x , float y){
        int z = x + (int)y;
        System.out.println(x + " + " + y + " = " + z);
    }

    Constructors(String name){
        System.out.println("Hi " +  name + ", I am your constructor");
    }

    Constructors(int... x){
        System.out.println(Arrays.toString(x));
    }

    public static void primitiveTester(int x){
        x = 50;
    }

    public static void main(String[] args) {
        int x = 10;
        primitiveTester(x);
        System.out.println(x);

        Constructors cs = new Constructors("shub");
        Constructors sum = new Constructors(15, 5);
        Constructors arbi = new Constructors(1,2,3,4);
    }
}
