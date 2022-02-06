package DavidBanas;

class A{
    void showName(){
        System.out.println("Name is A");
    }
}

public class AnonClass {
    public static void main(String[] args) {
        int x = 10;
        A obj = new A(){
            void showName(){
                System.out.println("Name is anon");
            }
        };
        obj.showName();

    }
}
