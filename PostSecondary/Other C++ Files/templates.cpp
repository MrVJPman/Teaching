#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;

/*
template<typename T>
Incorrect because the return type has to be T
#void Max(T a, T b){
  return a > b ? a:b;
} */

//Give us an example of a template 
template<typename T>
T Max(T a, T b){
  //if (a>b) : return a 
  //else : return b
  return a > b ? a:b;
} 

int main() {
  int num1 = 10, num2 = 5;
  double num3 = 10.1, num4 = 10.2;
  char char1 = 'e', char2 = 102;

  cout << "The larger value between " << num1 << " and " << num2 << " is " << Max(num1, num2) << endl; 
  cout << "The larger value between " << num3 << " and " << num4 << " is " << Max(num3, num4) << endl;
  cout << "The larger value between " << char1 << " and " << char2 << " is " << Max(char1, char2) << endl;
}