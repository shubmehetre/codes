#include <bits/stdc++.h>
using namespace std;

int main() {

  int y = 10;
  int *x = &y;
  int *arr[] = {x};

  cout << *arr[0] ;
}
