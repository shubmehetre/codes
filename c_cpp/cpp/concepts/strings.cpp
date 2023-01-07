#include <bits/stdc++.h>
using namespace std;

int main() {

  // All the basic things possible with strings. RUN.

  string demo = "String is a collection of characters.";
  string test;

  // take string from user
  cout << "Enter some text : " << endl;
  getline(cin, test);
  cout << endl;
  cout << "test = " << "\"" << test << "\"" << endl << endl;

  // length
  cout << "Length() test : " << test.length() << endl << endl;

  // append
  cout << "append(\" ok\") test:  " << test.append(" ok") << endl << endl;

  // insert characters
  test.push_back('A');
  cout << "push_back(\'A\') test:  " << test << endl << endl;

  // at
  cout << "at(0) and test[0] : " << test.at(0) << " and " << test[0]<< endl << endl;

  // begin n end
  cout << "*begin() and *(end()-1): " << *test.begin() << " and "
       << *(test.end() - 1) << endl
       << endl;

  // Reverse
  reverse(test.begin(), test.end());
  cout << "Reverse(begin(), end()) of test: " << test << endl << endl;

  // string to integer using stoi()
  string x = "10";
  string y = "30";
  cout << "String to integer using stoi()\n";
  cout << "(x=10) + (y=30) => " << stoi(x) + stoi(y) << endl << endl;

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
  cout << "character A (typecasted to int) gives ASCII of A => " << int(c) << endl << endl;
}
