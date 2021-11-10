package DavidBanas;

public class callMethodInsideSameClass {

    public void Method1(){
        System.out.println("from method 1");
    }

    public void haha(String[] args){
        Method1();
    }

}


