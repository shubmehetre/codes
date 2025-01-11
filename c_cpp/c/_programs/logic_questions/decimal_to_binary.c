#include <stdio.h>

int main(){

	int bin[32];
	int num;
	int i = 0;

	printf("Enter decimal no: ");
	scanf("%d", &num);

	while (num > 0) {
	
		int reminder = num % 2;
		bin[i] = reminder; i++;
		num = num / 2;
	}

	// Reverse array bin[]
	for(int i = 0; bin[i]; i++);
		int len = i;
		printf("Len of array is %d\n", len);
	for(int i = len; i >= 0; i--){
		printf("%d", bin[i]);

	}
	printf("\n");

}
