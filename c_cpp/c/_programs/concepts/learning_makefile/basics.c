#include<stdio.h>

void variables(){
	int x = 20;
	printf("This is a int %d\n",x);

}

void testing_sizeof(){

	int x = 10;
	char z = 'A';

	int size_int = sizeof(x);
	int size_char = sizeof(z);

	printf("Size of integer in C is %d\n", size_int);
	printf("Size of char in C is %d\n", size_char);

}

void while_loop(){
	printf("# While Loops");

	int i = 10;

	while(i > 0){
		printf("\n%d", i);
		i = i - 1;
	}
	printf("\n");

}
