#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;

// Simple class for student's attributes
class Student {
public:
  string name;
  int marks;
};

// sort logic
bool cmp(Student a, Student b) {

  // switching values if a<b i.e. sorting in decending order for ranklist
  if (a.marks < b.marks) {
    return false;
  }

  return true;
}

int main() {
  vector<Student> v;

  // adding students to vector
  v.push_back({"chopper", 88});
  v.push_back({"yamcha", 72});
  v.push_back({"grimjaw", 46});
  v.push_back({"aizen", 100});

  // sorting with cmp
  sort(v.begin(), v.end(), cmp);

  // just printing the sorted list
  cout << "RANK List:\n";
  for (int i = 0; i < v.size(); i++) {

    cout << "Rank " << i + 1 << " " << v[i].name << " with " << v[i].marks
         << " marks" << endl;
  }
}
