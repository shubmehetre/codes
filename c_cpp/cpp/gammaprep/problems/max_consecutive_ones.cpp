#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {

  vector<int> v = {1, 1, 0, 0, 1, 0, 1, 1, 1, 1}; // answer shud be 3

  int temp_max = 0, max = 0;

  for (int i = 0; i < v.size(); i++) {

    if (v[i] == 1) {
      temp_max += 1;
    }

    if (v[i] == 0) {
      if(temp_max > max){
        max = temp_max;
      }
        temp_max = 0;
    }

  }

  if (temp_max > max){ max = temp_max ;};

  cout << "Max consecutive 1s is : " << max;
}
