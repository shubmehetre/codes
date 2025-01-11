#include <stdio.h>

int main (){

	// 2^3 = 2 * 2 * 2 = 8
	// 2^4 = 2 * 2 * 2 * 2 = 16
	// 32, 64, 128 ...

	int num;
	int ans = 0;
	printf("Please enter a number: ");
	scanf("%d", &num);

	// Eg. 4

	while (num % 2 == 0 && num > 2) {
		num = num / 2; // 2/2=2
		ans = num % 2; // 2%2=0
		
	}

	if (ans == 0){
		printf("Yes its Power of 2\n");
	}else{
		printf("No its NOT Power of 2\n");
	}

}

