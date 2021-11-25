package DavidBanas;

public class ControlFlow {
    public static void main(String[] args) {

/*
// Switch cases with int
        int year = 1996;
        int month = 2;
        int numDays = 0;

        switch(month) {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                numDays = 31;
                break;

            case 4: case 6: case 9: case 11:
                numDays = 30;
                break;

            case 2:
                if(((year % 4 == 0) && !(year % 100 == 0)) || (year % 400 ==0))
                    numDays = 29;
                else numDays = 28;
                break;
        }
        System.out.println("Num of days " + numDays);
*/
/*

        // passing strings to switch

        for (int i = 0; i<5 ; i++ ){
            for(int j = 0; j<i+1 ; j++ ){
                System.out.print("* ");
            }
            System.out.println();
        }
        String asd = "RAM";

        switch (asd.toLowerCase()){
            case "ram":
                System.out.println("Ramrajya");
                break;
            case "krishna":
                System.out.println("gokul");
                break;
            case "shiva":
                System.out.println("kailas");
                break;
            default:
                System.out.println("go home");
                break;
        }
*/

        // for loops

        // printing start pattern(classic)
        int num = 4;

        for (int i = 0 ; i < num ; i++){
            for(int j = num+2 ; j>i ; j++){
                 
            }
            System.out.println();
        }


    }
}
