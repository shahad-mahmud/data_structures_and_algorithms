/**
* 22-04-2019
* This the implementation of Insertion sort algorithm
**/
#include <iostream>
using namespace std;

int main(){
	int array[] = {1, 20, 4, 7, 9, 2, 11, 52, -9, 23, -98, 17};
	int size = sizeof(array)/sizeof(array[0]);
	int i, j;

	for(i = 1; i < size; i++){
		j = i - 1;
		int key = array[i];

		while(j>=0 && key < array[j]){
			array[j+1] = array[j];
			j--;
		}

		array[j+1] = key;
	}

	for(i = 0; i < size; i++)
		cout<< array[i] << " ";


	return 0;
}