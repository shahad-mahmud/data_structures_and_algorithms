/**
* 21-04-2019
* This the implemention of Linear search algorithm
**/
#include <iostream>
using namespace std;

int main(){
  int array[] = {10,52,98,-96,35,14,8,9,65,33,47,55,12}; //the array with data
  int key; //the data to find
  int i;

  printf("%s", "Enter a number to find: ");
  scanf("%d", &key); //take the key as user input

  for(i = 0; i < 13; i++){
    if(array[i] == key){ //check each data if matches with the key
      printf("Data found at index %d\n", i);
      break; //stop further searching.
    }
  }

  if(i == 13){ //i = 13 means all the index has been searched but no match was found
    printf("%s\n", "data not found");
  }

  return 0;
}
