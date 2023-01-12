#include <bits/stdc++.h>
using namespace std;

// class is advanced version of a struct.
// We can have private and public fields.
class Student{
  private:
  int marks;
  public:
  Student(){
    cout << "Welcome the class Student\n\n";
  }

  string name;

  // Getters and Setters
  void setMarks(int x){
    marks = x;
  }
  int getMarks(){
    return marks;
  }

};

int main() {

  Student s1 ;
  s1.name = "Ram";
  s1.setMarks(88);

  cout << s1.name << "'s" << " marks => " << s1.getMarks() << endl;



}
