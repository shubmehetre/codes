#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {

  int T, score = 0;
  cin >> T;

  while (T > 0) {

    int N;
    cin>>N;
    string S = "";

    cout << "input about to take\n\n";
    // take input
    for (int i = 0; i < N; i++) {
      cin >> S[i];
    }

    for (int i = 0; i < S.length(); i++) {

      // conditions for lower cases alphabets
      if (S[i] >= 97 && S[i] <= 122) {
        if (S[i] != 97 && S[i] != 101 && S[i] != 105 && S[i] != 111 &&
            S[i] != 117) {
          score += 1;
        } else {
          score += 2;
        }
      }

      // conditions for upper case alphabets
      if (S[i] >= 65 && S[i] <= 90) {
        if (S[i] != 65 && S[i] != 69 && S[i] != 73 && S[i] != 79 &&
            S[i] != 85) {
          score -= 1;
        } else {
          score -= 2;
        }
      }

      // conditions for digits
      if (S[i] >= 48 && S[i] <=57){
        score += ((int)S[i]-48);
      }

    }
  }
  cout << score<< endl;
}
