#include <bits/stdc++.h>
using namespace std;

int main(){

  int input;
  cout << "Number pls: ";
  cin>>input;

  int facto = 1;

  for (int i = 1; i<=input ; i++){
    facto = facto * i;
  }

  cout << "Factorial of " << input << " is " << facto;

}
