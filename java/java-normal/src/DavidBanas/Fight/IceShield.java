package DavidBanas.Fight;

import java.util.Random;

public class IceShield extends Warrior{
    double shieldPercent;
    Random r = new Random();

    IceShield(String name, int health, int attackMax, int blockMax, double shieldPercent){
        super(name, health, attackMax, blockMax);
        this.shieldPercent = shieldPercent;
    }
    public int block(){
        double chance = r.nextDouble();
        if (chance <= shieldPercent){
            System.out.println("ICE SHIELD BLOCKED EVERYTHING!!!!!");
            return 1000;
        }else
            return 1 + (int)(Math.random() * ((attackMax - 1) + 1));
    }
}
