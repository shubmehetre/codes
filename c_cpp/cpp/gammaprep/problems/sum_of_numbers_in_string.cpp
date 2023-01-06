#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {

  int answer = 0;
  string capture;
  string x = "1abc23";

  for (int i = 0; i<x.size(); i++){
    if (x[i] >= '0' && x[i] <='9'){
      capture.push_back(x[i]);
    }else {
      if(capture!=""){
      answer += stoi(capture);
      capture ="";
      }
    }
  }

  if (capture != ""){
      answer += stoi(capture);
  }

  cout<< "answer : " << answer;


}
