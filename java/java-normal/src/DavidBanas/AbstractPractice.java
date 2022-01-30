package DavidBanas;

abstract class MainAbstract {
    public abstract String getName();
}

class GetInfo extends MainAbstract{
    @Override
    public String getName() {
        return "shub";
    }
}

public class AbstractPractice{
    public static void main(String[] args) {
        GetInfo o1 = new GetInfo();
        System.out.println(o1.getName());
    }
}



