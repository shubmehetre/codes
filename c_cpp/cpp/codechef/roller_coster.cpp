#include <iostream>
using namespace std;

int main() {
  int T, X, H;

  cin >> T;
  string arr1[T];

  for (int i = 0; i < T; i++) {
    cin >> X >> H;
    X >= H ? cout << "YES" : cout << "NO";
    cout << endl;
  }

  return 0;
}
