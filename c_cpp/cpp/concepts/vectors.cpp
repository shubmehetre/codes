#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {

  /*
    vector<int> vec = {1,2,3,4,5};

    cout << vec.begin()[1] << endl;
    auto y = vec.begin();

    cout << *(y+1) << endl;
    cout << "*(v.end()-1) is : "<< *(vec.end()-1);

    // v.end() = v.begin + n; hence to point to last element we need to do minus
    1
    */
  ///////////////////////////////////////////////////////

  /*
  vector<vector<int>> v(3, vector<int>(4, 0))

  for (int i = 0; i < v.size(); i++) {

    for (int j = 0; j < v[0].size(); j++) {
      cout << v[i][j] << " | ";
    }

    cout << endl;
  }
  */

  //////////////////////////////////////////////////
  ///
/*
 // INSERT
  vector<int> v = {1, 3, 4, 5};
  cout << "current vector: ";

  for (int i=0; i<v.size(); i++){
    cout << v[i] << " ";
  }

  cout << "\n\nAdding 1 at 1st index " << endl;
  // inserting elements at specific index
  v.insert(v.begin()+1, 2);

  for (int i=0; i < v.size(); i++) {
    cout << v[i] << " ";
  }
  cout<<""<<endl;

  // BACK element print
  cout << "\nPrint back element: "<< v.back()<< "\n";
*/
////////////////////////////////////////////////////////////
/*
  // ADD element to vector
  v.push_back(6);
  cout<<"\nPush 6:\n";
  for (int i=0; i < v.size(); i++) {
    cout << v[i] << " ";
  }
  cout<<""<<endl;

  // REMOVE element from vector
  v.pop_back();
  cout<<"\nPop 6:\n";
  for (int i=0; i < v.size(); i++) {
    cout << v[i] << " ";
  }
  cout<<""<<endl;
*/
//////////////////////////////////////////////////////////////////

  vector<int> v = {1,2,3};
  vector<int> z = {};

  // z[0] = v[0];
  z.insert(z.begin(), v[0]);

  cout<< z[0]<<endl;
  cout<< v[0];


}
