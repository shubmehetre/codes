#include <bits/stdc++.h>
using namespace std;

int main() {

  string test[] = {"asd", "zxc"};


  for (auto i : test) {
    cout << i << " ";
  }

  cout << "";


  for(int i = 0 ; i<2; i++){
    cout << " lol "<< *(test+i) ;
  }


  /*
  for (int i = 0; i< test->length(); i++){
    cout << test[i];
  }
  */
  cout << endl;
  cout << test->length();
  cout << endl;
  cout << test->size();
}
