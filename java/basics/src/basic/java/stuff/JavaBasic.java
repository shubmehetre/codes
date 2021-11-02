package basic.java.stuff;
import basic.home.BasicJava;
import java.util.Scanner;

public class JavaBasic {

    // method with return type
    public  int sum(int x , int y)
    {
        int sum;
        sum = x + y;
        return sum;

    }

    // a static method
    public static void very_static()
    {
        System.out.println("This is from a static method.");
    }

    public void StringTest(String[] name)
    {
        int i;
        for ( i = 0; i < name.length ; i++) {
            System.out.println(name[i]);
        }

    }



    public static void main(String [] args)
    {
        JavaBasic obj1 = new JavaBasic();

        Class c = JavaBasic.class;
        System.out.println(c.getClassLoader());
        System.out.println(String.class.getClassLoader() );
        // String and loop practice
        String[] name = new String[]{"Shubham Mehetre"};
        obj1.StringTest(name);

    }

}