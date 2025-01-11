#include <stdio.h>

int main(){

	int x = 10;
	//create a pointer
	int *ptr;

	// Assign address of int x to ptr
	ptr = &x;

	printf("Value of x by dereferencing pointer is %p\n", ptr);



}
