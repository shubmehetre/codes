#include <stdio.h>

int main(){

	printf("Enter a decimal: ");
	int deci;
	scanf("%d",&deci );

	printf("%d\n", deci << 1);

	// left bit shift doubles the value. while right halfs it.
	// printf("%lu", sizeof(deci));
}
