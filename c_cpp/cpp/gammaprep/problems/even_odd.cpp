#include <algorithm>
#include <bits/stdc++.h>
#include <sys/types.h>

using namespace std;

int main() {
  bool isRunning = true;

  while (isRunning) {
    cout << "\nEnter a number: ";
    int n;
    cin >> n;
    if (n % 2 == 0) {
      cout << "Even!";
    } else {
      cout << "Odd!";
    }

    cout << "\nDo you want to continue(y/n): ";

    char userInput;
    cin >> userInput;

    if (userInput == 'y') {
      continue;
    } else {
      isRunning = false;
      cout << "\nThe End. Press return to close\n";
    }
  }
}
