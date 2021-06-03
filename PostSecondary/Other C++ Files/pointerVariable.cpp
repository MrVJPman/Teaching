#include <iostream>
#include <string>
using namespace std;

int main() {
  string food = "Pizza";  // A string variable
  string* ptr = &food;  // A pointer variable that stores the address of food

  // Output the value of food
  cout << food << "\n";
  cout << *ptr << "\n";

  // Output the memory address of food
  cout << &food << "\n";
  cout << ptr << "\n";

  
  *ptr = "chicken";
  cout << food << "\n"; //chicken
  cout << *ptr << "\n"; //chicken
  cout << &food << "\n"; //memory address
  cout << ptr << "\n"; //memory address

  food = "steak";
  cout << food << "\n"; //steak
  cout << *ptr << "\n"; //steak
  cout << &food << "\n"; //memory address
  cout << ptr << "\n"; //memory address
  return 0;
}
