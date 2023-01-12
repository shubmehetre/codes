#include <bits/stdc++.h>
#include <utility>
#include <vector>
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

  vector<test> v1 ;
  v1.push_back(t1);
  v1.push_back(t2);
  // cout<<v1[0]; this will give error
  cout<<v1[0].name;


  vector<int> v2;
  v2.push_back(1);
  v2.push_back(2);
  cout<<v2[0];


}
