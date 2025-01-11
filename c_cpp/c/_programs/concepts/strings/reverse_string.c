#include <stdio.h>

int main(){

	printf("Enter a string to reverse: ");
	char arr[100];
	scanf("%s", arr);

	int i;

	for(i=0; arr[i]; i++);

	for(int j = i; j>=0; j-- ){

		printf("%c", arr[j]);
	}

	printf("\n");

}
