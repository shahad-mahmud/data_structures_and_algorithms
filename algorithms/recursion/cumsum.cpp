#include <iostream>
using namespace std;

int cum_sum(int *a, int i)
{
    if (i < 0)
        return 0;
    int sum = a[i] + cum_sum(a, i - 1);
    a[i] = sum;
    return sum;
}

int main()
{
    int list[5] = {1, 2, 3, 4, 5};

    cum_sum(list, 4);

    for (int i = 0; i < 5; i++)
    {
        cout << list[i] << " ";
    }
    cout << endl;

    return 0;
}