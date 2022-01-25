package DavidBanas;
interface Tester3 {
    int x = 10;

    static void getName(){
        System.out.println("my name raul");
    }
    default void getID(){
        System.out.println("my id is 101");
    }
}

public class Tester2 implements Tester3{

    public static void main(String[] args) {
        Tester2 t1 = new Tester2();
        t1.getID();
    }

}
