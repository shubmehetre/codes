package DavidBanas;

public class Tester2 {
    public static void main(String[] args) {
        int x = 10;
        String num1 = "10";

        double y = 10.5;
        String num2 = "10.5";

        System.out.println(Integer.valueOf(x));
        System.out.println(Integer.valueOf(num1));
        System.out.println(Double.valueOf(y));
        System.out.println(Double.valueOf(num2));

        System.out.println();

        System.out.println((Integer.valueOf(x)).getClass());
        System.out.println((Integer.valueOf(num1)).getClass());
        System.out.println((Double.valueOf(y)).getClass());
        System.out.println((Double.valueOf(num2)).getClass());
    }
}