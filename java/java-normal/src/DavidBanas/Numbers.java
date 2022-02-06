package DavidBanas;

public class Numbers {
    public static void main(String[] args) {
        String num1 = "10.5";
        String num2 = "10";

        int x = 10;
        String y = Integer.toString(x);

        double d = 10.10;
        String z = Double.toString(d);

        System.out.println("Str to Integer: " + Integer.parseInt(num2));
        System.out.println("Str to Double : " + Double.parseDouble(num1) );
        System.out.println("Integer to str : " + y);
        System.out.println("Double to Str: " + d);



    }
}
