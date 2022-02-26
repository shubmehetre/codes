package DavidBanas.Fight;

public class WarriorGame {
    public static void main(String[] args) throws InterruptedException {
        Warrior subzero = new IceShield(
                "Subzero", 1200, 380, 450, .20);
        Warrior scorp = new CriticalHitter(
                "Scorpian", 800, 420, 400, .10);

        Battle.startFight(subzero,scorp);
    }
}
