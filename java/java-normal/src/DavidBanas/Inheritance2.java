package DavidBanas;

class MasterClass{
    void showName(){
        System.out.println("My Name Is chika-chika slim shady");
    }
}

public class Inheritance2 extends MasterClass{
    @Override
    void showName(){
        System.out.println("Rahul, name to suna hoga");
    }

    public static void main(String[] args) {
        Inheritance2 test1 = new Inheritance2();
        test1.showName();

        MasterClass master1 = new Inheritance2();
        master1.showName();

        MasterClass master2 = new MasterClass();
        master2.showName();

        Object master3 = new MasterClass();
        ((MasterClass) master3).showName();

//      MasterClass master4 = (MasterClass) master3;
//      master4.showName();
    }
}