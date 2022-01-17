package DavidBanas.Fight;

import java.util.SortedMap;

public class Battle {
    public static void startFight(Warrior w1, Warrior w2) throws InterruptedException {
        while (true){
            if(getAttackResult(w1,w2).equals("GAME OVER")){
                System.out.println("\n======GAME OVER=======");
                break;
            }
            if(getAttackResult(w2,w1).equals("GAME OVER")){
                System.out.println("\n======GAME OVER=======");
                break;
            }
        }
    }

    public static String getAttackResult(Warrior wA , Warrior wB) throws InterruptedException {
        int wAAttackAmt = wA.attack();
        int wBBlockAmt = wB.block();

        int dmg2WarB = wAAttackAmt - wBBlockAmt;

        if (dmg2WarB > 0){
            wB.health = wB.health - dmg2WarB;
        }else dmg2WarB = 0;

        System.out.printf("%s attacks %s and deals "
                + "%d damage\n",wA.getName() , wB.getName() , dmg2WarB);

        System.out.printf("%s has %d health left\n\n"
                , wB.getName(), wB.health);

        Thread.sleep(1000);

        if (wB.health <= 0 ){
            System.out.printf("%s has died and %s"
            + " is Victorious", wB.getName(), wA.getName());
            return "GAME OVER";
        }
        else return "Fight Again";

    }


}
