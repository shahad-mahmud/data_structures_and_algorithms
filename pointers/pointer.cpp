#include <iostream>
using namespace std;

int main(){
    int a = 2;
    int* ptr, normal;  

    normal = 5;
    ptr = &normal;

    cout << normal <<endl << ptr <<endl;
    // get value using pointer
    cout << *ptr << endl;
    cout << &ptr << endl;

    cout << &a;

    return 0;
}