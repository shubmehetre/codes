#include <stdio.h>

int main() {

  char name[32];
  printf("Enter you name: ");

  scanf("%[^\n]%*c", &name);

  printf("Hello, %s\n", name);
}
