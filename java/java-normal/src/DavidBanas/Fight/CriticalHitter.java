package DavidBanas.Fight;

import java.util.Random;

public class CriticalHitter extends Warrior{
    double critPercent;
    Random rand = new Random();

    public CriticalHitter(String name, int health,
                          int attackMax, int blockMax, double critPercent){
        super(name, health, attackMax, blockMax);
        this.critPercent = critPercent;
    }

    public int attack(){
        double chance = rand.nextDouble();
        if (chance <= critPercent){
            System.out.println("CRITICAL HIT!!!!!");
            return 1000;
        }else
            return 1 + (int)(Math.random() * ((attackMax - 1) + 1));
    }
}
