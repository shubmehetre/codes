#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;

// sort will randomly make any numbers in v as a and b
// but a will always be behind b
// false => switch position, true => keep position same
bool cmp(int a, int b){

  // here if a < b we switch. here this is a decending sort
  if (a < b ){
    return false;
  }
  return true;

}

int main() {

  vector<int> v = {6, 7, 8, 1, 2, 3, 4, 5};

  sort(v.begin(), v.end(), cmp);

  for (int i = 0; i < v.size(); i++) {
    cout << v[i] << " ";
  }
}
