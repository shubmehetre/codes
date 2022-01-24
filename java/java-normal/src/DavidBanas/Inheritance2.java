package DavidBanas;

class MasterClass{
     void showName(){
        System.out.println("My Name Is chika-chika slim shady");
    }
    static void showID(){
        System.out.println("My Id is 101");
    }
}

public class Inheritance2 extends MasterClass{

    static void showID(){
        System.out.println("static overried func");
    }

    public static void main(String... args) {
        Inheritance2 test1 = new Inheritance2();
        test1.showName();

        MasterClass master1 = new Inheritance2();
        master1.showName();

        MasterClass master2 = new MasterClass();
        master2.showName();

        Object master3 = new MasterClass();
        ((MasterClass) master3).showName();

        Inheritance2.showID();
//      MasterClass master4 = (MasterClass) master3;
//      master4.showName();
    }
}