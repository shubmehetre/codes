#include <stdio.h>

void calculate_the_maximum(int n, int k) {
	// For AND
	int max = 0;
	// n = 5 - 1,2,3,4,5
	for (int i = 1; i<=n; i++){
		for (int j = i+1; j<=n; j++){
			if(max < (i & j) && ((i & j) < k)){
				max = i & j;
			}else {
				continue;
			}
		}
	}
	int max2 = 0;
	// n = 5 - 1,2,3,4,5
	for (int i = 1; i<=n; i++){
		for (int j = i+1; j<=n; j++){
			if(max2 < (i | j) && ((i | j) < k)){
				max2 = i | j;
			}else {
				continue;
			}
		}
	}
	int max3 = 0;
	// n = 5 - 1,2,3,4,5
	for (int i = 1; i<=n; i++){
		for (int j = i+1; j<=n; j++){
			if(max3 < (i ^ j) && ((i ^ j) < k)){
				max3 = i ^ j;
			}else {
				continue;
			}
		}
	}
	printf("%d\n%d\n%d", max, max2, max3);
}

int main() {
	int n, k;

	scanf("%d %d", &n, &k);
	calculate_the_maximum(n, k);

	return 0;
}

