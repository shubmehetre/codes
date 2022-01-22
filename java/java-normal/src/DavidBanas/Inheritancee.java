package DavidBanas;

import java.util.Objects;
import java.util.Scanner;

public class Inheritancee extends child2 {

    int main_num = 10;
    public static void main(String[] args) {
        System.out.println("from child's main func");

        child2 c2 = new child2();
        Object obj = new Inheritancee();

        Inheritancee hh = (Inheritancee) obj;

        // object casting
        System.out.println(((Inheritancee) obj).main_num);

        String name = c2.getName();
        System.out.println("name is " + name);

        int id = c2.getId();
        System.out.println("id is " + id);

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
    int child2_num = 10;
    public int getId(){
        return 101;
    }
    public String getName(){
        return "Overrided name";
    }
}