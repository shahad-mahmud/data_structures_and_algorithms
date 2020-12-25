#include <iostream>
using namespace std;

class Item{
public:
    int data;
    Item* next;
};

// I'll creat a simple linked list with 3 items.
int main(){
    // at first declear the items
    Item* item1 = NULL;
    Item* item2 = NULL;
    Item* item3 = NULL;

    item1 = new Item();
    item2 = new Item();
    item3 = new Item();

    // assign data and next items
    item1->data = 1;
    item1->next = item2; // this will point the item2

    item2->data = 2;
    item2->next = item3; // this will point the item3

    item3->data = 3;
    item3->next = NULL; // it means this is the last item.

    return 0;
}