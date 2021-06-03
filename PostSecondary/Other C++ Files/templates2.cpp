// Input Manipulators
 // manipulator.cpp

 #include <iostream>
 #include <iomanip>
 using namespace std;

template <typename T>
T max(T x, T y) 
{
  return (x > y) ? x : y;
}

int main() {
  //Error, the 20,16, -2, -4, 'a', "A" IS ambiguous as C++ doesn't know the type
  std:cout << max(20, 16); 
  std::cout << max(-2, -4); 
  std::cout << max('a', 'A');
  return 0;
}