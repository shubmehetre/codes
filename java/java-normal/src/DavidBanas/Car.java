package DavidBanas;

public abstract  interface Car {
    void gas();
    void brake();
    void clutch();
    void bike();
    default void peddle(){
        System.out.println("in interface");
    }
}

class bmw extends Tester implements Car {
    @Override
    public void gas() {
        System.out.println("accelerating");
    }

    @Override
    public void brake() {
        System.out.println("stopping");
    }

    @Override
    public void clutch() {
        System.out.println("Shifting gear");
    }

    @Override
    public void bike() {
        System.out.println("from bike");
    }


    public static void main(String[] args) {
        Car c1 = new bmw();
        c1.gas();
        c1.clutch();
        c1.brake();
        c1.bike();

        c1.peddle();

        Tester t1 = new Tester();
        System.out.println(t1.getName());
    }
}