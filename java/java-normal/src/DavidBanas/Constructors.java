package DavidBanas;
class ConstructorsPractice{

    public int width = 0;
    public int height = 0;

    ConstructorsPractice(int x , int y){
        width = x;
        height = y;
    }

    int getArea(){
        return width * height;
    }
    public static void main(String[] args) {

        int sum = new ConstructorsPractice(10 , 20).getArea();
        System.out.println(sum);
    }
}
