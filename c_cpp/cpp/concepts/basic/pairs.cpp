#include <bits/stdc++.h>
#include <utility>
#include <vector>
using namespace std;

class Student{
public:
  pair <string, int> p;

  pair <vector<string>, int> q;

};

int main() {

  // using class
  Student s1;
  s1.p.first="Ram";
  s1.p.second = 99;

  // anything is possible xD here first part of pair is a vector, second is int.
  s1.q.first.push_back("shub");
  s1.q.second = 99;


  // standalone pair in main
  pair<string, int> p1;

  p1.first = "Shub";
  p1.second = 100;

  // vector of pairs
  vector<pair <string, int>> v;

  v.push_back(p1);

  cout << v[0].first;
  cout << v[0].second;



}
