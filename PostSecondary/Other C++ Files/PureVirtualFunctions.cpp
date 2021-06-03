#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;


class Wind {
  public:
    //Pure virtual function
    virtual void increase(int amount) = 0;

    //Virtual function destructor
    virtual ~Wind() {}
};

class Tornado : public Wind {
  double velocity;
  public:
    Tornado(double v) {
      velocity = v;
    }

    //Must override pure virtual functionn   
    virtual void increase(int value) {
      velocity += value;
    }

    ~Tornado() {}
};

int main() {
  //Cann not create an object of an abstract base class type
  //Wind* wind_array[2] = {new Tornado(66.5), new Wind()};  
  Wind* wind_array[2] = {new Tornado(66.5), new Tornado(12)};

  for (int i=0; i<2; i++) {
    wind_array[i]->increase(10);
    delete wind_array[i];
  }
  return 0;
}

