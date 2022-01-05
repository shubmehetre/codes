package DavidBanas;

/**
 * Author : Shubham A. Mehetre
 * Purpose: Practicing variables in Java
 */
class Variables {

    int classVar = 10; // instance variables
    static int staticClassVar = 20; // class variables

    public void classVarTester(){
        System.out.println("in tester1 static var = " + classVar);
    }

    public void StaticClassVarTester(){
        System.out.println("in tester1 static var = " + staticClassVar);
    }

    public static void main(String [] args) {


        Variables v1 = new Variables();
        Variables v2 = new Variables();

        System.out.println("class var access using v1 is : " + v1.classVar);
        System.out.println("class var access using v2 is : " + v2.classVar);
        v1.classVar++;
        System.out.println("class var ++ using v1 is : " + v1.classVar);
        v2.classVar++;
        System.out.println("class var ++ using v2 is : " + v2.classVar);

        System.out.println();

        System.out.println("static var access using v1 is : " + staticClassVar);
        System.out.println("static var access using v2 is : " + staticClassVar);
        staticClassVar++;
        System.out.println("static var ++ using v1 is : " + staticClassVar);
        staticClassVar++;
        System.out.println("static var ++ using v2 is : " + staticClassVar);


        // fields/variables in java
        int myInt = 10;
        float myFloat = 123.1f;
        double myDouble = 123.141234235234523452345d;
        short myShort = 123;
        boolean myBool = true;
        byte myByte = 127;
        char myChar = 'A';
        int testStatic = 1000;

/*
        // create obj of Operators class and calling method
        Operators op1 = new Operators();
        op1.testPro();
*/



/*
        // find limit of a datatye using datatye.MAX_VALUE
        System.out.println("Max limit of a float: " + Float.MAX_VALUE);
        System.out.println("Max limit of an int: " + Integer.MAX_VALUE);
*/

/*
        // find data type of variable using .getClass
        String getClassTester = "this is a string";
        System.out.println("Finding datatype of var using .getClass() : " + getClassTester.getClass());
*/

/*
        // ways to create a string
        String str1 = "Hello, World!";
        String str2 = new String("Hello, World from str2");
        System.out.println(str2);
*/

/*
        // type casting, cast any data type to any other
        double newDouble = 420.6969;
        int doubleToInt = (int) newDouble;
        System.out.println("type casted double to int: " + doubleToInt);
*/


/*
        // .toString creates JUST string from another datatypes
        String strFromInt = Integer.toString(myInt);
        String strFromShort = Short.toString(myShort);
        System.out.println("str from int : " + strFromInt);
        System.out.println("str from short : " + strFromShort);
*/

/*
        // String to any other type using parse. String shud be convertable.
        String zxc = "100";
        System.out.println(Integer.parseInt(zxc));

        // .parse<any type> : Using to convert only STRING to any data type
        int testingParse = Integer.parseInt(strFromInt);
        System.out.println(testingParse);
*/
/*
        String test2 = new String("haha");
        System.out.println(test2.getClass());

        Integer test3 = 20;
        int test1 = 5;
        System.out.println(test1);
*/

    }
}
