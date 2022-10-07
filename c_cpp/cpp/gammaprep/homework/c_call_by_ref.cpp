// LINK: https://practice.geeksforgeeks.org/problems/c-call-by-reference/1

//{ Driver Code Starts
// Initial Template for C++

#include <iostream>
using namespace std;

// } Driver Code Ends
// User function Template for C++

void reverse_dig(int &a, int &b) {
  int x =
}

void swap(int &a, int &b) {
  // Add your code here.
  a = b;
  b = a;
}

//{ Driver Code Starts.

int main() {
  int t;
  cin >> t;
  while (t--) {
    int a, b;
    cin >> a >> b;

    reverse_dig(a, b);
    swap(a, b);
    cout << a << " " << b << endl;
  }
  return 0;
}
// } Driver Code Ends
