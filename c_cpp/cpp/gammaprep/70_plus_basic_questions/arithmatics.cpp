#include<bits/stdc++.h>
using namespace std;

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<int> cppOperators(int A, int B) {
        // code here
        vector<int> answer;

      answer.push_back(A+B);
      answer.push_back(A*B);
      if (A>B){
      answer.push_back(A-B);
      answer.push_back(A/B);
    }else {
      answer.push_back(B-A);
      answer.push_back(B/A);
    }

      return answer;

    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int A, B;
        cin >> A >> B;
        Solution ob;
        vector<int> ans = ob.cppOperators(A, B);
        for (int u : ans) cout << u << "\n";
    }
}
// } Driver Code Ends
