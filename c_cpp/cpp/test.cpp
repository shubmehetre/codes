#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {

  vector<int> v = {2, 3, 4, 5};

  v.insert(v.begin()+1, 7);

  for (int i; i < v.size(); i++) {
    cout << v[i] << " ";
  }
}
// 