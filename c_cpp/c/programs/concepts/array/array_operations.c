#include <stdio.h>

int main (){
	int list[10];

	for (int i = 0; i<10; i++){
		list[i] = i;
	}
	for (int i = 0; i<10; i++){
		printf("%d",list[i]);
	}
	printf("\n");
}
