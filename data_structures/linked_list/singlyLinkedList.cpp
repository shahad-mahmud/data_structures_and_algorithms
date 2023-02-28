#include <iostream>
using namespace std;

class LinkedList{
private:
    struct node{
        int data;
        node* next;
    };
    node* head = NULL;
    node* previous_node = NULL;
    int sizeOfList = 0;

public:
    void add(int data){
        node* newNode = (node*) malloc(sizeof(node));
        newNode->data = data;
        newNode->next = NULL;

        if(head == NULL){
            head = newNode;
        }

        if(previous_node != NULL){
            previous_node->next = newNode;
        }
        previous_node = newNode;
        sizeOfList++;
    }

    void traverse_list(){
        node* iterator = head;

        while(iterator!=NULL){
            cout << iterator->data << " ";
            iterator = iterator->next;
        }
    }

    int size(){
        return sizeOfList;
    }
};

int main(){
    LinkedList list;

    list.add(5);
    list.add(35);
    list.add(60);

    cout << "Values of the list: ";
    list.traverse_list();
    cout << endl;

    cout << "Size of the List is: " << list.size() << endl;

    return 0;
}