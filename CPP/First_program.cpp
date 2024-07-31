# include <iostream>
using namespace std;

int main() {
    int a1[5] = {1,98,23,21,3};

    int* ptra1 = a1;

    a1[0]= 33;
    a1[1] = 12;

    cout << &a1 << endl;
    cout << &a1[0] << endl;
    cout << (&a1[0] + 1 == &a1[1]) << endl;
    cout << (&a1[1] + 1 == &a1[2]) << endl;
    cout << (&a1[2] + 1 == &a1[3]) << endl;
    cout << (&a1[3] + 1 == &a1[4]) << endl;

    cout << *ptra1 << endl;
    

return 0; }