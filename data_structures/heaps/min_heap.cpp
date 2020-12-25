#include <iostream>
using namespace std;

const int HEAP_SIZE = 10;

int s = 0;

void bubble_up(int* heap, int i){
    // check if heap property is reserved
    int parent = (i-1)/2;
    if(heap[parent] > heap[i]){
        // heap property not reserved. bubble up the node.
        int temp = heap[parent];
        heap[parent] = heap[i];
        heap[i] = temp;

        // now check if the parent is reserving the heap property or not
        bubble_up(heap, parent);
    }
}

void bubble_down(int* heap, int i){
    //get the left and right child
    int left_child = heap[2*i + 1];
    int right_child = heap[2*i + 2];

    //check if the parent is greater than the children
    if(heap[i] > left_child || heap[i] > right_child){
        //get the smallest child
        if(left_child < right_child){
            // swap with left child
            int temp = heap[i];
            heap[i] = heap[i];
            heap[2*i + 1] = temp;

            //continue checking
            bubble_down(heap, 2*i + 1);
        }else{
            // swap with right child
            int temp = heap[i];
            heap[i] = heap[i];
            heap[2*i + 2] = temp;

            //continue checking
            bubble_down(heap, 2*i + 2);
        }
    }
}

void extract(int* heap){
    //swap the root and the last node
    int temp = heap[0];
    heap[0] = heap[s-1];
    heap[s-1] = temp;

    //now remove the last node
    s--;

    bubble_down(heap, 0);
}

void insert(int* heap, int key){
    heap[s] = key; //add the node
    bubble_up(heap, s);
    s++;
}

void extract(){
    cout << s;
}

int get_root(int* heap){
    return heap[0];
}

int main(){
    int heap[HEAP_SIZE];

    insert(heap, 2);
    insert(heap, 5);
    insert(heap, 1);
    extract(heap);


    for (int i = 0; i < s; i++)
    {
        cout << heap[i] << " ";
    }
    cout << endl;

    cout << get_root(heap) << endl;
    

    return 0;
}