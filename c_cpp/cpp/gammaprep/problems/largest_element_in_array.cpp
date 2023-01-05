#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {

  vector<int> v = {1,1,2,2,3,6,3,2};

  int large = 0;

  for (int i=0 ; i<v.size(); i++){
    if (v[i] > large){
      large = v[i];
    }
  }

  cout << "Largest element: " << large;


}
