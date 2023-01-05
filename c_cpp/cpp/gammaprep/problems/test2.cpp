#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {

  vector<int> v = {4,1,2,3};

  int rot = 1;
  while(rot--){
    v.push_back(*(v.begin()));
  }

  for (auto i = 0 ;i< v.size() ; i++) {

    cout<<v[i] << " ";

  }


}
