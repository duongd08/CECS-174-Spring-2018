#include <iostream>

#include <iostream>
#include <iomanip>
#include <limits>
using namespace std;

float capacitor()
{
  int i, element, circuit;
  float sum0 = 0, sum1 = 0, sum2 = 0;
  float * capacitance;
  
  cout << "Enter the amount of capacitor: ";
  cin >> element;
  capacitance = new (nothrow) float[element];
  
  if(capacitance == nullptr)
  {
    cout << "Memory couldn't be allocated.\n";
    exit(1);
  }
  else
  {
    cout << "Enter the capacitance for each capacitor.\n";
    for(i = 0; i < element; i++)
    {
      cout << i+1 << ": ";
      cin >> capacitance[i];
    }
    cout << "\n";
    
    cout << "Choose circuit connection.\n";
    cout << "|  1:Series  |  2: Parallel  |\n";
    cin >> circuit;
    
    switch(circuit)
    {
      case 1:
        for(i = 0; i < element; i++)
        {
          sum0 += 1/capacitance[i];
          sum1 = 1/sum0;
        }
        return sum1;
        delete[] capacitance;
        break;
      case 2:
        for(i = 0; i < element; i++)
        {
          sum2 += capacitance[i];
        }
        return sum2;
        delete[] capacitance;
        break;
    }
  }
}

float resistor()
{
  int i, element, circuit;
  float sum3 = 0, sum4 = 0, sum5 = 0;
  float * resistor;
  
  cout << "Enter the amount of capacitor: ";
  cin >> element;
  resistor = new (nothrow) float[element];
  
  if(resistor == nullptr)
  {
    cout << "Memory couldn't be allocated.\n";
    exit(1);
  }
  else
  {
    cout << "Enter the capacitance for each capacitor.\n";
    for(i = 0; i < element; i++)
    {
      cout << i+1 << ": ";
      cin >> resistor[i];
    }
    
    cout << "Choose circuit connection.\n";
    cout << "|  1:Series  |  2: Parallel  |\n";
    cout << ">> ";
    cin >> circuit;
    
    switch(circuit)
    {
      case 2:
        for(i = 0; i < element; i++)
        {
          sum3 += 1/resistor[i];
          sum4 = 1/sum3;
        }
        return sum4;
        delete[] resistor;
        break;
      case 1:
        for(i = 0; i < element; i++)
        {
          sum5 += resistor[i];
        }
        return sum5;
        delete[] resistor;
        break;
    }
  }
}

int main()
{
  int component;
  float valueCapacitor, valueResistor;
  
  cout << "Welcome to capacitor and resistor calculator!\n";
  
  do
  {
    cout << "\n";
    cout << "|  1: Capacitor  |  2: Resistor  |  0: Exit  |\n";
    cout << ">> ";
    cin >> component;
    
    switch(component)
    {
      case 0:
        cout << "\n";
        cout << "Exiting...\n";
        exit(0);
        break;
      case 1:
        cout << "\n";
        valueCapacitor = capacitor();
        cout << "The value of capacitance is: " << setprecision(2) << valueCapacitor << "F\n";
        break;
      case 2:
        cout << "\n";
        valueResistor = resistor();
        cout << "The value of resistance is: " << setprecision(2) << valueResistor << " Ohm\n";
        break;
      default:
        cout << "\n";
        cout << "Invalid input.\n";
    }
  }while(component != 0);
  
  return 0;
}
