#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

vector<long long int> find(int L, int B, int H) {
  // Code here
  vector<long long int> ans;
  long long int l = (long long)L;
  long long int b = (long long)B;
  long long int h = (long long)H;
  ans.push_back(2 * (l * b + b * h + l * h));
  ans.push_back(l * b * h);

  return ans;
}


int main (){
  vector<long long int> ans = find(29077, 62884, 99973);

  cout << ans[0] << " " << ans[1];
}
