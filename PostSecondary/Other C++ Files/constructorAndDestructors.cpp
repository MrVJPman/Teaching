#include <iostream>

using namespace std;

class Base{
  int bval;

  public :
    Base(): bval(7){}
    Base(int b):  bval(b){}
    virtual ~Base() {cout << "B" << bval;}
};

class Derived:public Base{
  int dval;

  public :
    Derived(): Base(1){dval=0;}
    Derived(int d):Base(4){dval=d;}
    ~Derived() {cout << "D" << dval;}
};

int main() {
  Derived d2(9); //D9B4
  Base b; //B7
  Derived d; //D0B1
  Base b2(5); //B5

  //Output is
  //B5D0B1B7D9B4

  //LIFO order when it comes to deconstructing objects
  //The earliest created object is deconstructed last
  //The latest created object is deconstructed first

  //Derived Deconstructors is finished calling before calling the base class
}
