package DavidBanas;
class ConstructorsPractice{

    public int width = 0;
    public int height = 0;

    ConstructorsPractice(){
//      this(10 , 15);                                      // this will call the parameterized constructor
        System.out.println("Hi from default constructor");
    }

    ConstructorsPractice(int x , int y){
        this();                                             // this has to be 1st statement in the constructor body
        System.out.println("addition is = " + (x+y));
    }

    public static void main(String[] args) {
        ConstructorsPractice obj1 = new ConstructorsPractice(10, 15);
    }
}
