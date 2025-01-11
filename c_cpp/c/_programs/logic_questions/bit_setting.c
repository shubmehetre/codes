/////////////?INCOMPPLETE
#include <stdio.h>
#define F fflush(stdout)


int main() {


	printf("Enter a binary num: "); F;
	int bin;
	int i = 0;
	int ans[64];
	scanf("%d", &bin);

	printf("\nEnter position to set: "); F;
	int pos;
	scanf("%d", &pos);

	bin = bin | 1 << pos;


	while (bin > 0) {

		int reminder = bin % 2;
		ans[i] = reminder; i++;
		bin = bin / 2;
	
	}
	int len = sizeof(ans) / sizeof(ans[0]);

	printf("Length is %d\n", len);


	for (int i = len; i >= 0; i--){
		printf("%d",ans[i]);
	}

}
