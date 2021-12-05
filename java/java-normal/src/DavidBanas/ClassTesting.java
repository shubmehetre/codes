package DavidBanas;

public class ClassTesting {

    int test1;
    int test2;
    String test3;

    ClassTesting(int test1Value, int test2Value, String strValue){
        test1 = test1Value;
        test2 = test2Value;
        test3 = strValue;
    }

    public void newTest1Value(int x){
        test1 = x;
        System.out.println("changed value of test1 = " + test1);
    }
    public void newTest2Value(int y){
        test2 = y;
        System.out.println("changed value of test2 = " + test2);
    }
    public void newTest3Value(String z){
        test3 = z;
        System.out.println("changed value of test3 = " + test3);
    }
}
