package DavidBanas.Fight;

public class WarriorGame {
    public static void main(String[] args) throws InterruptedException {
        Warrior subzero = new Warrior(
                "Subzero", 1200, 380, 450);
        Warrior scorp = new CriticalHitter(
                "Scorpian", 1000, 450, 400, .15);

        Battle.startFight(subzero,scorp);
    }
}
