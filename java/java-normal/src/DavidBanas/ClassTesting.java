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

class ClassTesting2 extends ClassTesting{

    int test4;

    ClassTesting2(int test1Value, int test2Value, String strValue, int test4Value) {
        super(test1Value, test2Value, strValue);
        test4 = test1Value;
    }


    public void newTest4Value(int a){
        test4 = a;
        System.out.println("changed value of test4 = " + test4);
    }
}