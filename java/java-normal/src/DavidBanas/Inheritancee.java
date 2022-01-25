package DavidBanas;

import java.util.Objects;
import java.util.Scanner;

public class Inheritancee extends child2 {

    int main_num = 10;
    public static void main(String[] args) {

        Inheritancee hh = new Inheritancee();

    }
}

class child1 {
    int child_id;
    public String getName() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Name: ");
        String name = sc.next();
        return name;
    }
}

class child2 extends child1{
    child2(){
        System.out.println("child 2 constructor");
    }
    int child2_num = 10;
    public int getId(){
        return 101;
    }
    public String getName(){
        return "Overrided name";
    }
}