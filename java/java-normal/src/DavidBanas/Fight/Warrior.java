package DavidBanas.Fight;

class HAHA{
    int x = 10;
}

// When a new warrior is created(initialized) we give it some attributes and functions
public class Warrior {
    protected String name = "";
    public int health = 0;
    public int attackMax = 0;
    public int blockMax = 0;

    public Warrior(){
        this("Default", 100, 100, 100); // if warrior create without any args
    }
    public Warrior(String name, int health, int attackMax, int blockMax){
        this.setName(name); // as name is protected, we have to use setter
        this.health = health;
        this.attackMax = attackMax;
        this.blockMax = blockMax;
    }

    public int attack(){
        return 1 + (int)(Math.random() * ((attackMax - 1) + 1)); }

    public int block(){
        return 1 + (int)(Math.random() * ((blockMax - 1) + 1));
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getName(){
        return name;
    }
}