package DavidBanas;

public interface Interfaces {
    int x = 10;
    final String LED = "LED";

    String testStr();

}

class GoHome implements Interfaces{

    @Override
    public String testStr() {
        return "shub";
    }
}