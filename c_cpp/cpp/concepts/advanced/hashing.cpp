#include <bits/stdc++.h>
using namespace std;


int main(){
  unordered_set<int> set1;

  set1.insert(1);
  set1.insert(1);
  set1.insert(2);

  cout << *set1.find(1) << endl;
  cout << *set1.find(2);
}
