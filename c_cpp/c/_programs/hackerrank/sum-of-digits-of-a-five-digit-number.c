// https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number/problem?isFullScreen=true
#include <stdio.h>

int main(){

	int n;
	scanf("%d", &n);
	int sum = 0;

	// we are going to keep slicing n
	// so untill its > 0 we run the loop
	while (n > 0) {
		// Get reminder and keep adding it to sum
		int reminder = n % 10;
		sum = sum + reminder;
		// remove that last digit (reminder) from n
		n /= 10;
	}
	printf("%d", sum);
}
