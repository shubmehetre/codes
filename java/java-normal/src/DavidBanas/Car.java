package DavidBanas;

import DavidBanas.Fight.Battle;

public interface Car {
    void gas();
    void brake();
    void clutch();
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

    public static void main(String[] args) {
        Car c1 = new bmw();
        c1.gas();
        c1.clutch();
        c1.brake();

        Tester t1 = new Tester();
        System.out.println(t1.getName());
    }
}