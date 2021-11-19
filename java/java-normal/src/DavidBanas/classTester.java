package DavidBanas;

public class classTester {

   public static void main(String[] args) {
      System.out.println("calling class var from Variables class in classTester");
      System.out.println("Value: " + Variables.testClassVar);

      Variables.testClassVar++;

      classTester obj = new classTester();
      obj.staticCaller();

   }

   public void staticCaller(){

      System.out.println("calling from another method after increment in previous");
      System.out.println("Value: " + Variables.testClassVar);
   }

}
