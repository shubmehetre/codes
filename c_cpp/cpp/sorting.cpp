#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
using namespace std;

struct Student{
  string name;
  int marks;
};

// index of a will always be less than b.
// This permutation is done by sort() behind the scenes
bool dict(Student a, Student b){
  if (a.marks > b.marks ){
    return true;
  }
  else return false;
}

int main(){

  vector<Student> s;

  s.push_back({"shub", 90});
  s.push_back({"bosco", 70});
  s.push_back({"jane", 80});

  cout << s[1].marks << endl;

  // third parameter of sort is a bool function.
  // This function takes 2 arguments, 2 elements for the ds that we are sorting
  // lets say a and b. Index of a will always be less than b.
  // We need to use this bool func for some DS like dict.where sort(s.begin(), s.end()) is not enough.
  // true means values will not swap. false means the opposite.
  sort(s.begin(), s.end(), dict);

  for (int i = 0; i<s.size(); i++){
    cout << s[i].name << " scored " << s[i].marks << endl;
  }

  // for (auto i : s){
  //   cout << s[i].marks<< endl;
  // }
}
