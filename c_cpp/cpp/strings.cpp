#include <algorithm>
#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {

  string test;

  // take string from user
  cout << "Enter some text for var test: " << endl;
  getline(cin, test);
  cout << endl;
  cout << "$test  = " << test << endl << endl;

  // length
  cout << "Length() test : " << test.length() << endl << endl;

  // append
  cout << "append(\" ok\") test:  " << test.append(" ok") << endl << endl;

  // at
  cout << "at(0) test: " << test.at(0) << endl << endl;

  // Reverse
  reverse(test.begin(), test.end());
  cout << "Reverse of $test: " << test << endl << endl;

  // string to integer using stoi()
  string x = "10";
  string y = "30";
  cout << "10 + 30 = " << stoi(x) + stoi(y) << endl << endl;

  // integer to string using to_string()
  int i = 1;
  int j = 2;
  int k = 3;

  cout << "1 + 2 + 3 (for ints) = " << i + j + k << endl << endl;
  cout << "1 + 2 + 3 (for chars)= "
       << to_string(i) + to_string(j) + to_string(k) << endl
       << endl;

  // type casting
  char c = 'A';
  cout << "A (typecasted to int) = "<<int(c) << endl << endl;
}
