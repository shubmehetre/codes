package basic.java.stuff;

public class AddOverlaod {

    public void add(int i, int j) throws ArithmeticException{
        System.out.println(i + j);
    }

    public void add(int i, int j, int k) throws ArithmeticException {
        System.out.println(i + j + k);
    }

    public void add(double i, double j) throws ArithmeticException {
        System.out.println(i + j);
    }

    public static void main(String[] args) {

        AddOverlaod obj = new AddOverlaod();

        obj.add(5 ,5);
        obj.add(5,5,5);
        obj.add(5.2,4.8);
    }

}
