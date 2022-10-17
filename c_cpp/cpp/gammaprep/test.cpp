#include <bits/stdc++.h>
using namespace std;

class Test{
  public:
    int testing(int x[]){

    x[0] = 10;

    return 0;
  }
};

int main(){

  int x = 10;
  Test obj;
  int i[] ={1,2,3};

  obj.testing(i);

  cout << i[0];
  return 0;

}
