#include <algorithm>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

int main() {

  int n = 28;

  string ans = "";

  // adding 30 0s to string
  for (int i = 0; i < 30; i++){
    ans.push_back('0');
  }
//  cout << "string is : " << ans;

  int i = 0;
  while (n>0) {
    if (n%2 == 1){
      ans[i] = '1';
    }
    n /= 2;
    i++;
  }
  reverse(ans.begin(), ans.end());

  cout << ans;

}
