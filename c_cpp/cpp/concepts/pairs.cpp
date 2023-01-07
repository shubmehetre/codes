#include <bits/stdc++.h>
#include <utility>
#include <vector>
using namespace std;

int main() {

  pair<string, int> p1;

  p1.first = "Shub";
  p1.second = 100;

  vector<pair <string, int>> v;

  v.push_back(p1);

  cout << v[0].first;
  cout << v[0].second;



}
