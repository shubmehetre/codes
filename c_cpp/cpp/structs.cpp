#include <bits/stdc++.h>
#include <utility>
using namespace std;

struct test{
  int cost;
  string name;
};

int main(){

  test t1;

  t1.cost = 10000;
  t1.name = "Nike Air Jordans";

  test t2 = {12000, "Adidas"};

  cout << t1.name << endl;
  cout << t2.name << endl;

  pair<string,int> test1 = {"shub", 26};

  cout<<test1.first;


}
