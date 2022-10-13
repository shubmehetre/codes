#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {
  int n, max = 0, temp;

  cin >> n;

  // storing the n inputs into a vector
  for (int i = 0; i < n; i++) {
    cin >> temp;
    if (temp > max) {
      max = temp;
    }
  }

  cout << max;
}
