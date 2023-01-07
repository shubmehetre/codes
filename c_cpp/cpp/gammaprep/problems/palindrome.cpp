#include <algorithm>
#include <bits/stdc++.h>
#include <cstring>
#include <string>

using namespace std;

// Palindrome
int main() {

  int main = 2;

  if (main / 10 == 0) {
    cout <<  "Palindrome";
  }else {
  char temp[to_string(main).length()];
  int helper = 0;

  for (int i = to_string(main).length() - 1; i >= 0; i--) {
    temp[helper] = to_string(main)[i];
    helper++;
  }

  if (to_string(main) == temp) {
    cout << "Palindrome";
  } else {
    cout << "NOT";
  }

  }

}
