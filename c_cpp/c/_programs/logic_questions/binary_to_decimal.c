// Binary to Decimal Program
#include <stdio.h>
#define F fflush(stdout)

int main(){

	printf("Enter a binary number: "); F;

	// Get binary number
	int bin_num;
	int magic = 2;
	int reminder = 0;
	scanf("%d", &bin_num);

	// 1 2 4 8 16 32
	int decimal_num = 0;

	// for 1, seperate case created
	reminder = bin_num % 10;
	decimal_num = decimal_num + reminder * 1;
	bin_num /= 10;

	while (bin_num > 0) {

		reminder = bin_num % 10;
		decimal_num = decimal_num + reminder * magic;
		magic *= 2;
		bin_num /= 10;
	}

	printf("\nDecimal number is : %d\n", decimal_num);


}
