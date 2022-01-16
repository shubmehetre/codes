package DavidBanas;

public class NestedClasss {

    String outerString = "Outer field";
    static String outerStaticString = "Static Outer field";

    class InnerClass {
        void accessMembers(){
            System.out.println("From InnerClass: " + outerString);
            System.out.println("From InnerClass: " + outerStaticString);
        }
    }

    static class StaticInnerClass{
        void accessMembers(){
            System.out.println("From StaticInnerClass: " + outerStaticString);
//          System.out.println(outerString);        // Error: Cannot make static reference to non-static field 'outerString'
        }
    }

    public static void main(String[] args) {
        NestedClasss n1 = new NestedClasss();
        NestedClasss.InnerClass o1 = n1.new InnerClass();
        o1.accessMembers();

        StaticInnerClass s1 = new StaticInnerClass();
        s1.accessMembers();

        String hello = "Hello";

        class Tester{
            void printString(){
                System.out.println("From Local class: " + hello);
            }
        }

        Tester t1 = new Tester();
        t1.printString();
    }
}
