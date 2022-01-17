package DavidBanas.Fight;

public class WarriorGame {
    public static void main(String[] args) throws InterruptedException {
        Warrior subzero = new Warrior(
                "Subzero", 1200, 380, 450);
        Warrior scorp = new Warrior(
                "Scorpian", 1000, 450, 400);

        Battle.startFight(subzero,scorp);
    }
}
