#include <bits/stdc++.h>
#include <unistd.h>

using namespace std;

int main() {
  int T, sum = 0;
  cin >> T;
  while (T--) {

    int N;
    cin >> N;

    if (N > 9 || sum > 9) {

      while (N > 0) {
        sum += N % 10;
        N /= 10;
      }
      N = sum;
    } else {
  cout << N;
}
  }
cout << sum;
}
