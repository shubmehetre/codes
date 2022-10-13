// URL: https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
  int t;

  // number of tc
  cin >> t;

  while (t--) {
    int n,d,temp;
    // number of elements in array and rotate by
    cin >> n >> d;

    vector<int> arr;
    for (int i = 0; i < n; i++) {
      cin >> temp;
      arr.push_back(temp);
    }

    vector<int> ans;

    for (int i = d; i<n; i++ ){
      ans.push_back(arr[i]);
    }
    for (int i=0; i<d; i++){
      ans.push_back(arr[i]);
    }

    // printing the answer
    for (int i = 0; i<n;i++){
      cout << ans[i] << " ";
    }
    cout << endl;

  }


}
